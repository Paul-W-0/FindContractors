from django.contrib.auth.models import User
from django.db import models
class Profile(models.Model):
    experience = models.TextField()
    about_me = models.CharField(max_length=240)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_a_contractor = models.BooleanField(default=True)