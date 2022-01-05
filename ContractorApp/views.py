from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from .models import Contractor, Job, Profile, SecurityReport
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import ContractorSignUpForm, UserTypeForm, WorkSignUpForm, ProfileSetup, JobCreationForm, SecurityReportForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core import mail
@login_required
def home(request):
    try:
        if Contractor.objects.filter(user=request.user).get(is_a_contractor=False):
            query = Contractor.objects.filter(user=request.user).get(is_a_contractor=False)
            return render(request, 'home.html', { 'query':query, } )
        else:
            return HttpResponseBadRequest()
    except Contractor.DoesNotExist:
        if Contractor.objects.filter(user=request.user).get(is_a_contractor=True):
            jobcontext = Job.objects.all()
            return render(request, 'home.html', { 'jobcontext':jobcontext, } )
        elif User.is_superuser or User.is_staff:
            return HttpResponseRedirect('/security/reports/')
        else:
            return HttpResponseBadRequest()
@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_bound: # Using is_bound() here instead of is_valid because theres no need to save the form.
            user_choice = request.POST.get('choice_type') # Refer to the UserTypeForm class in forms.py for information.
            if user_choice == '1':
                return HttpResponseRedirect('/signup_contractor_finish/')
            elif user_choice == '2':
                return HttpResponseRedirect('/signup_company_finish/')
            else:
                return HttpResponseRedirect('/signup/')
        else:
            return HttpResponse('Please check your information, and try again.')
    else:
        form = UserTypeForm()
        return render(request, 'signup.html', { 'form':form, } )
@csrf_protect
def signup_contractor_finish(request):
    if request.method == 'POST':
        signup_form = ContractorSignUpForm(request.POST)
        if signup_form.is_valid():
            save_form = signup_form.save()
            save_form.save()
            get_user = User.objects.all().last()
            Contractor.objects.create(user=get_user, is_a_contractor=True)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse('We encountered a problem when processing your request, please check you information and try again.')
    else:
        form = ContractorSignUpForm()
        return render(request, 'contractor_signup.html', { 'form':form, } )
@csrf_protect
def signup_company_finish(request):
    if request.method == 'POST':
        signup_form = WorkSignUpForm(request.POST)
        if signup_form.is_valid():
            save_form = signup_form.save()
            save_form.save()
            get_user = User.objects.all().last()
            Contractor.objects.create(user=get_user, is_a_contractor=False) # Assign the newest user in the database to either be a Contractor or Company.
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponse('We encountered a problem when processing your request, please check your information and try again.')
    else:
        form = WorkSignUpForm()
        return render(request, 'work_signup.html', { 'form':form, } )
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
@login_required
def profile(request):
    try:
        query = Contractor.objects.filter(user=request.user).get(is_a_contractor=False)
        context = Profile.objects.filter(user=request.user)
        return render(request, 'account/profile.html', { 'context':context, 'query':query, } )
    except Contractor.DoesNotExist:
        context = Profile.objects.filter(user=request.user)
        return render(request, 'account/profile.html', { 'context':context, } )
@csrf_protect
@login_required
def setup_profile(request):
    obj = Profile.objects.filter(user=request.user)
    if obj.exists():
        return HttpResponseRedirect('/update_profile/')
    else:
        if request.method == 'POST':
            form = ProfileSetup(request.POST)
            if form.is_valid:
                save_form = form.save()
                save_form.user = request.user
                save_form.save()
                return HttpResponseRedirect('/profile/')
            else:
                return HttpResponse('There was a problem proccessing your request!')
        else:
            form = ProfileSetup()
            return render(request, 'account/profile_setup.html', { 'form':form } )
@csrf_protect
@login_required
def update_profile(request):
    if request.method == 'POST':
        obj = Profile.objects.get(user=request.user)
        form = ProfileSetup(request.POST, instance=obj) # Update the form for the current user only.
        if form.is_valid():
            save_form = form.save()
            save_form.save()
            return HttpResponseRedirect('/profile/')
        else:
            return HttpResponse('There was a problem proccessing your request!')
    else:
        form = ProfileSetup()
        return render(request, 'account/update_profile.html', { 'form':form } )
@csrf_protect
@login_required
def job_create(request):
    try:
        if Contractor.objects.filter(user=request.user).get(is_a_contractor=False):
            if request.method == "POST":
                form = JobCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Please check your information, and try again!')
            else:
                form = JobCreationForm()
                return render(request, 'job_create.html', { 'form':form, } )
    except Contractor.DoesNotExist:
        if Contractor.objects.filter(user=request.user).get(is_a_contractor=True):
            return HttpResponseForbidden()
@csrf_protect
@login_required
def report_security_problem(request):
    if request.method == 'POST':
        form = SecurityReportForm(request.POST)
        if form.is_valid():
            form.save()
            connection = mail.get_connection()
            connection.open()
            email = mail.EmailMessage(
                'A Thank You from the Find.Contractors Team!',
                'We appreciate your submission to helping build a safer community in the online world!',
                '', # Need to add a company email here
                request.user.email,
                connection=connection
            )
            email.send()
            connection.close()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Please make sure all required fields are filled out properly.')
    else:
        form = SecurityReportForm()
        return render(request, 'report_security.html', { 'form':form, } )
@login_required
def reports(request):
    if User.is_staff == True or User.is_superuser:
        context = SecurityReport.objects.all()
        return render(request, 'security_reports.html', { 'context':context, } )
    else:
        return HttpResponseForbidden()