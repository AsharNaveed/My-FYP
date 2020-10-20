from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Employee

def employee_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Employees')
        instance.groups.add(group)
        Employee.objects.create(
            employee_user_id=instance,
            Full_Name=instance.username,
        )
        print('Profile Created')


post_save.connect(employee_profile, sender=User)