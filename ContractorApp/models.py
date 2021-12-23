from django.contrib.auth.models import User
from django.db import models
class Profile(models.Model):
    experience = models.TextField()
    about_me = models.CharField(max_length=240)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_a_contractor = models.BooleanField(default=True) # The default should always be True so that when users are created they don't get assigned the wrong user type.
class Job(models.Model):
    title = models.CharField(max_length=110)
    description = models.TextField()
    work_duties = models.TextField()
    preferred_certifications = models.TextField()
    minimum_qualifications = models.TextField()
class SecurityReport(models.Model):
    title = models.CharField(max_length=110)
    description = models.TextField()
    explanation = models.TextField()
    steps_to_reproduce = models.TextField()
    