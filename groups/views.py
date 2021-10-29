from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.db import IntegrityError
from . import models
# Create your views here.
from groups.models import Group,GroupMember


class CreateGroupView(LoginRequiredMixin,generic.CreateView):  #creating a group
    fields=('name','description')
    model=Group


class SingleGroupView(generic.DetailView):   #how will each group look like
    model=Group
    

class ListGroupView(generic.ListView):   #shows the list of all available groups made
    model=Group
    
    

class CreateGroupMemberView(LoginRequiredMixin,generic.UpdateView):
    fields=('name')
    model=GroupMember
    
class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    #redirect the url to that single group once you join the group
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})
 #try to get a group or return 404
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))
 #creating a group member with user=self.user and group=group
        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,"Warning, already a member of {}".format(group.name))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)

    


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
                         ).get() 

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)
