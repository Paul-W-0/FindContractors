from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contractor, Profile, Job
registered = [Profile, Contractor, Job]
admin.site.register(registered)
admin.site.unregister(Group) # Users are granted permissions based on whether or not they are a contractor (check the Contractor model for more info).