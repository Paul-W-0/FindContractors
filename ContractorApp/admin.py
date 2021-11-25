from django.contrib import admin
from .models import Profile

registered = [Profile]
admin.site.register(registered)