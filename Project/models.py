from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    DEPARTMENT = (
        ('Psychologist', 'Psychologist'),
        ('Physiotherapist', 'Physiotherapist'),
        ('Consultant', 'Consultant'),
        ('Intern', 'Intern')
    )
    EDUCATION = (
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters')
    )
    employee_user_id = models.OneToOneField(User, null=True, blank=False, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=200, null=True)
    Email_Address = models.EmailField(max_length=200, null=True)
    CNIC = models.CharField(max_length=200, null=True)
    Password = models.CharField(max_length=200, blank=True, null=True)
    Confirm_Password = models.CharField(max_length=200, blank=True, null=True)
    Phone_No = models.CharField(max_length=200, null=True)
    Department = models.CharField(max_length=200, null=True, choices=DEPARTMENT)
    Designation = models.CharField(max_length=200, null=True)
    Salary = models.CharField(max_length=100, null=True)
    Experience = models.CharField(max_length=200, null=True)
    Education = models.CharField(max_length=200, null=True, choices=EDUCATION)
    Profile_Pic = models.ImageField(default="Male Profile Avatar.png", null=True, blank=True)
    Date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Full_Name

class Leave(models.Model):
    LEAVES = (
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('None', 'None'),
    )
    Any_Leave = models.CharField(max_length=100, null=True, choices=LEAVES)

    def __str__(self):
        return self.Any_Leave

class Attendance(models.Model):
    CHECKED_IN = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    CHECKED_OUT = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    STATUS = (
        ('Working', 'Working'),
        ('End', 'End'),
        ('Extra Shift', 'Extra Shift'),
        ('On Leave', 'On Leave'),
    )
    MARK = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    )
    EARLY_GOING = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    LATE_COMMING = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    HOURS_UTILIZED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    Employee_Name = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    Check_In = models.CharField(max_length=50, null=True, choices=CHECKED_IN)
    Time_In = models.CharField(max_length=100, null=True)
    Check_Out = models.CharField(max_length=50, null=True, choices=CHECKED_OUT)
    Time_Out = models.CharField(max_length=100, null=True)
    Early_Going = models.CharField(max_length=50, blank=True, null=True, choices=EARLY_GOING)
    Late_Comming = models.CharField(max_length=50, blank=True, null=True, choices=LATE_COMMING)
    leave = models.ForeignKey(Leave, blank=True, null=True, on_delete=models.SET_NULL)
    Status = models.CharField(max_length=100, null=True, choices=STATUS)
    FullHours_Utilized = models.CharField(max_length=50, null=True, choices=HOURS_UTILIZED)
    Mark_Attendance = models.CharField(max_length=100, null=True, choices=MARK)
    Date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Mark_Attendance

class Payroll(models.Model):
    ATT_PERCENTAGE = (
        ('100%', '100%'),
        ('70%', '70%'),
        ('50%', '50%'),
        ('Less than 50%', 'Less than 50%')
    )
    MONTH_YEAR = (
        ('January 2020', 'January 2020'),
        ('February 2020', 'February 2020'),
        ('March 2020', 'March 2020'),
        ('April 2020', 'April 2020'),
        ('May 2020', 'May 2020'),
        ('June 2020', 'June 2020'),
        ('July 2020', 'July 2020'),
        ('August 2020', 'August 2020'),
        ('September 2020', 'September'),
        ('October 2020', 'October 2020'),
        ('November 2020', 'November 2020'),
        ('December 2020', 'December 2020'),
    )

    Employee_Name = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    #if Mark_Attendance in Attendance == 'Present':
       # getattr()
   # Mark_Attendance = models.ForeignKey(Attendance, null=True, on_delete=models.SET_NULL)
    Month_Year = models.CharField(max_length=100, null=True, choices=MONTH_YEAR)
    Basic_Salary = models.CharField(max_length=100, null=True)
    Per_Day_Wage = models.IntegerField(null=True)
    Leave_Utilized = models.ForeignKey(Leave, null=True, on_delete=models.SET_NULL)
    Four_LeaveSpent_Deduction = models.IntegerField(null=True)
    No_of_Presents = models.CharField(max_length=50, null=True)
    Att_Percentage = models.CharField(max_length=50, null=True, choices=ATT_PERCENTAGE)
    Final_Pay = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Month_Year
