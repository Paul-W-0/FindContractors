from django import forms
from django.forms.widgets import PasswordInput, RadioSelect
from django.contrib.auth.models import User
from .models import Profile, Job
from django.contrib.auth.forms import UserCreationForm as UserCreationForm
class UserTypeForm(forms.Form):
    choice_type = forms.ChoiceField(widget=RadioSelect, choices=( ( 1, 'Im a Contractor' ), ( 2, 'Looking for a Contractor' ) ), required=True)
    class Meta:
        fields = ('choice_type')
class ContractorSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=75)
    company = forms.CharField(max_length=75)
    type_of_work = forms.CharField(max_length=220)
    certifications = forms.CharField(max_length=220)
    is_insured = forms.ChoiceField(widget=RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Select whether or not you are insured: '}), choices=( (1, 'YES'), (2, 'NO') ), required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=35, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'company', 'type_of_work', 'certifications', 'is_insured')
class WorkSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=35, required=True)
    company = forms.CharField(max_length=75)
    type_of_work = forms.CharField(max_length=150)
    requires_insurance = forms.ChoiceField(widget=RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Does your company require the contractor to be insured: '}), choices=( (1, 'YES'), (2, 'NO') ), required=True)
    class Meta:
        model = User
        fields = ('username', 'company', 'email', 'type_of_work', 'requires_insurance')
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=PasswordInput, max_length=40, required=True)
class ProfileSetup(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'experience', 'about_me' )
class JobCreationForm(forms.ModelForm):
    choice = ( (1, 'Construction'), (2, 'Security'), (3, 'Information Technology'), (4, 'Retail'), (5, 'Warehouse'), (6, 'Online Only') )
    job_type = forms.ChoiceField(choices=choice)
    class Meta:
        model = Job
        fields = ('title', 'description', 'job_type', 'work_duties', 'preferred_certifications', 'minimum_qualifications')