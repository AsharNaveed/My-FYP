from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_user, name="logout_user"),

    path('', views.home, name="home"),
    path('empDashboard/', views.empdashboard, name="emp_dashboard"),

    path('empprofile/<int:pk>/', views.empprofile, name="empprofile"),
    path('empprofile_settings/', views.empprofilesetting, name="empprofilesettings"),

    path('user/', views.user, name="user"),
    path('attendance/', views.attendance, name="attendance"),
    path('report/', views.report, name="att_report"),
    path('payroll/', views.payroll, name="payroll"),

    path('add_attform/', views.add_attendace, name="add_attform"),
    path('update_attform/<int:pk>/', views.update_attendance, name="update_attform"),
    path('delete_attform/<int:pk>/', views.delete_attendance, name="delete_attform"),

    path('add_empform/', views.add_employee, name="add_empform"),
    path('update_empform/<int:pk>/', views.update_employee, name="update_empform"),
    path('delete_empform/<int:pk>/', views.delete_employee, name="delete_empform"),

    path('add_payrollform/', views.add_payroll, name="add_payrollform"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="projects/Password_Reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="projects/Password_Reset_Sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="projects/Password_Reset_Form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="projects/Password_Reset_Done.html"),
         name="password_reset_complete"),


]
