from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contractor, Profile
registered = [Profile, Contractor]
admin.site.register(registered)
admin.site.unregister(Group)