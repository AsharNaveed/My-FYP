from django.shortcuts import render, redirect
from .models import *
from .forms import AttForm, CreateUserForm, AddEmpForm, PayrollForm, EmpEditForm
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import inlineformset_factory
#from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

@unauthenticated_user
def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # emp = Employee.objects.all()
        if form.is_valid():
            employee_user_id = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login_page')

    context = {'form': form}
    return render(request, 'projects/Registration Form.html', context)

@unauthenticated_user
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'projects/Login Form.html')

    context = {}
    return render(request, 'projects/Login Form.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url=login_page)
@admin_only
def home(request):
    employees = Employee.objects.all()
    attendances = Attendance.objects.all()
    payrolls = Payroll.objects.all()
    leaves = Leave.objects.all()

    total_employee = employees.count()
    total_leave = leaves.count
    total_attendance = attendances.count()
    total_payroll = payrolls.count()

    context = {'employees': employees, 'attendances': attendances,
               'payrolls': payrolls, 'total_leave': total_leave,
               'total_employee': total_employee, 'total_attendance': total_attendance,
               'total_payroll': total_payroll}

    return render(request, 'projects/Dashboard.html', context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Employees'])
def empdashboard(request):
    return render(request, 'projects/EmpDashboard.html')


@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def user(request):
    all_employees = Employee.objects.all()
    return render(request, 'projects/UMS.html', {'employees': all_employees})

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Employees'])
def empprofile(request, pk):
    leave = Leave.objects.all()
    total_leave = leave.count()

    leave_spent = request.user.employee.attendance_set.filter(Mark_Attendance='Leave')
    leave_utilize = leave_spent.count()

    emp = Employee.objects.get(id=pk)

    attendances = Attendance.objects.filter(Employee_Name=Employee.objects.get(id=pk))

    context = {'Employees': emp, 'attendance': attendances,
               'total_leave': total_leave, 'leave_spent': leave_utilize}
    return render(request, 'projects/EmpProfile.html', context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Employees'])
def empprofilesetting(request):
    employee = request.user.employee
    form = EmpEditForm(instance=employee)

    if request.method == 'POST':
        form = EmpEditForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'projects/EmpProfile_Settings.html', context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def attendance(request):
    attendances = Attendance.objects.all()
    #attendance_count = Attendance.objects.filter(Attendance="Leave")
    context = {'attendance': attendances}
    return render(request, 'projects/AMS.html', context)

@allowed_users(allowed_roles=['Admin'])
def report(request):
    att = Attendance.objects.all()
    context = {'Attendance_Report': att}
    return render(request, 'projects/Reports.html', context)


@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def payroll(request):
    # anyvariable = an array
    # store all payroll information through formulas on attendance table and store it in anyvariable.
    # pass that anyvariable in render

    # calculating per day wage
    # per_day_wage = Salary/30
    emp = Employee.objects.all()
    context = {'Employee': emp}
    return render(request, 'projects/PMS.html', context)


@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def add_attendace(request):
    # AttFormSet = inlineformset_factory(Employee, Attendance, fields=('Attendance_No', 'Employee_Name', 'Check_In', 'Check_Out', 'Status',
    # 'FullHours_Utilized', 'Attendance'))
    # all_employees = Employee.objects.get(id=pk)
    form = AttForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = AttForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance')

    context = {'form': form}
    return render(request, 'projects/Attform.html', context)


@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def update_attendance(request, pk):
    attn = Attendance.objects.get(id=pk)
    form = AttForm(instance=attn)

    if request.method == 'POST':
        form = AttForm(request.POST, instance=attn)
        if form.is_valid():
            form.save()
            return redirect('attendance')
    context = {'form': form}
    return render(request, 'projects/Attform.html', context)


@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def delete_attendance(request, pk):
    attn = Attendance.objects.get(id=pk)
    if request.method == "POST":
        attn.delete()
        return redirect('attendance')
    context = {'item': attn}
    return render(request, 'projects/DeleteAtt.html', context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def add_employee(request):
    form = AddEmpForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = AddEmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')

    context = {'form': form}
    return render(request, 'projects/AddEmpForm.html', context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def update_employee(request, pk):
    demp = Employee.objects.get(id=pk)
    form = EmpEditForm(instance=demp)

    if request.method == 'POST':
        form = EmpEditForm(request.POST, instance=demp)
        if form.is_valid():
            form.save()
            return redirect('user')
    context = {'form': form}
    return render(request, 'projects/AddEmpForm.html', context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def delete_employee(request, pk):
    demp = Employee.objects.get(id=pk)
    if request.method == "POST":
        demp.delete()
        return redirect('user')
    context = {'item': demp}
    return render(request, 'projects/DeleteEmp.html', context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['Admin'])
def add_payroll(request):
    attendances = Attendance.objects.all()
    payrolls = Payroll.objects.all()

    form = PayrollForm()
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll')

    context = {'form': form, 'All_attendances': attendances, 'All_payrolls': payrolls}
    return render(request, 'projects/PylForm.html', context)