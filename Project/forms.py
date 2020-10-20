from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class AttForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['Employee_Name',
                  'Time_In',
                  'Check_In',
                  'Time_Out',
                  'Check_Out',
                  'Status',
                  'FullHours_Utilized',
                  'Mark_Attendance']

class AddEmpForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'Full_Name', 'Email_Address', 'Password', 'Confirm_Password']
        exclude = ['user']

class EmpEditForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['CNIC', 'Phone_No', 'Department', 'Designation', 'Salary',
                  'Education', 'Experience']

class PayrollForm(ModelForm):
    class Meta:
        model = Payroll
        fields = ['Employee_Name',
            'Month_Year',
            'Basic_Salary',
            'No_of_Presents',
            'Per_Day_Wage',
            'Four_LeaveSpent_Deduction', 'Att_Percentage', 'Final_Pay']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        #User = Employee
        fields = ['username', 'email', 'password1', 'password2']
