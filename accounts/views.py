from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.NewUserForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"
