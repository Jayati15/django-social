from django.contrib import admin
from .import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model=models.GroupMember
    
admin.site.register(models.Group)
#edit the models at the same page as the parent model(tabular inline class)