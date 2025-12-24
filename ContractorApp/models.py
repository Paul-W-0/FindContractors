from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxLengthValidator

class Profile(models.Model):
    experience = models.TextField(validators=[MaxLengthValidator(5000)])
    about_me = models.CharField(max_length=240)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_a_contractor = models.BooleanField(default=True) # The default should always be True so that when users are created they don't get assigned the wrong user type.

class Job(models.Model):
    employer = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=110)
    description = models.TextField(validators=[MaxLengthValidator(5000)])
    work_duties = models.TextField(validators=[MaxLengthValidator(5000)])
    preferred_certifications = models.TextField(validators=[MaxLengthValidator(2000)])
    minimum_qualifications = models.TextField(validators=[MaxLengthValidator(2000)])
    slug = models.SlugField(unique=True, blank=True, null=True)
    contractor_name = models.CharField(max_length=175, default='')
    contractor_experience = models.TextField(null=True, validators=[MaxLengthValidator(5000)])
    chosen_contractor_name = models.CharField(max_length=175, default='')

class SecurityReport(models.Model):
    title = models.CharField(max_length=110)
    description = models.TextField(validators=[MaxLengthValidator(5000)])
    explanation = models.TextField(validators=[MaxLengthValidator(5000)])
    steps_to_reproduce = models.TextField(validators=[MaxLengthValidator(5000)])

class JobApplication(models.Model):
    name = models.CharField(max_length=175)
    related_experience = models.TextField(validators=[MaxLengthValidator(5000)])