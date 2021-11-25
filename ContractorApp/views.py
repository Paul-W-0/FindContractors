from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import ContractorSignUpForm, UserTypeForm, WorkSignUpForm, ProfileSetup
from django.contrib.auth import logout
from .forms import ProfileSetup
from django.contrib.auth.models import Group
@login_required
def home(request):
    return render(request, 'home.html', {  } )
@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_bound:
            user_choice = request.POST.get('choice_type')
            if user_choice == '1':
                return HttpResponseRedirect('/signup_contractor_finish/')
            elif user_choice == '2':
                return HttpResponseRedirect('/signup_company_finish/')
            else:
                return HttpResponseRedirect('/signup/')
        else:
            return HttpResponse('Please check your information, and try again.')
    else:
        form = UserTypeForm
        return render(request, 'signup.html', { 'form':form, } )
@csrf_protect
def signup_contractor_finish(request):
    if request.method == 'POST':
        signup_form = ContractorSignUpForm(request.POST)
        if signup_form.is_valid():
            save_form = signup_form.save()
            save_form.save()
            return HttpResponseRedirect('/login/')
        else:
            # print(form.errors)
            return HttpResponse('We encountered a problem when processing your request, please check you information and try again.')
    else:
        form = ContractorSignUpForm
        return render(request, 'contractor_signup.html', { 'form':form, } )
@csrf_protect
def signup_company_finish(request):
    if request.method == 'POST':
        signup_form = WorkSignUpForm(request.POST)
        if signup_form.is_valid():
            save_form = signup_form.save()
            save_form.save()
            return HttpResponseRedirect('/login/')
        else:
            # print(form.errors)
            return HttpResponse('We encountered a problem when processing your request, please check your information and try again.')
    else:
        form = WorkSignUpForm
        return render(request, 'work_signup.html', { 'form':form, } )
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
@login_required
def profile(request):
    context = Profile.objects.filter(user=request.user)
    return render(request, 'account/profile.html', { 'context':context } )
@csrf_protect
@login_required
def setup_profile(request):
    obj = Profile.objects.filter(user=request.user)
    if obj.exists():
        return HttpResponseRedirect('/update_profile/')
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
        form = ProfileSetup
        return render(request, 'account/profile_setup.html', { 'form':form } )
@csrf_protect
@login_required
def update_profile(request):
    if request.method == 'POST':
        obj = Profile.objects.get(user=request.user)
        form = ProfileSetup(request.POST, instance=obj)
        if form.is_valid():
            save_form = form.save()
            save_form.save()
            return HttpResponseRedirect('/profile/')
        else:
            return HttpResponse('There was a problem proccessing your request!')
    else:
        form = ProfileSetup
        return render(request, 'account/update_profile.html', { 'form':form } )