from django.urls import path
from ContractorApp import views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.signup, name="signup"),
    path('signup_contractor_finish/', views.signup_contractor_finish, name='signup_contractor_finish'),
    path('signup_company_finish/', views.signup_company_finish, name='signup_company_finish'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile, name='profile'),
    path('profile_modification/', views.setup_profile, name='setup_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('jobs/create/', views.job_create, name="job_create"),
    # Security Vulnerability Report Links:
    path('security/', views.report_security_problem, name='report_security_problem'),
    path('security/reports/', views.reports, name='reports'),
    # Password Reset Links: 
    path('password_reset/', PasswordResetView.as_view(
        template_name='account/password_reset.html',
        email_template_name='account/password_reset_email.html',
        subject_template_name='account/password_reset_subject.txt',
        success_url='/login/'), name='password_reset'
    ),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'),
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html',
        success_url='/account/reset/done/'),
        name='password_reset_confirm'
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]