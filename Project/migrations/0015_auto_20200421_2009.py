# Generated by Django 3.1.dev20200305084444 on 2020-04-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0014_auto_20200420_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payroll',
            old_name='Employee',
            new_name='Employee_Name',
        ),
        migrations.RemoveField(
            model_name='payroll',
            name='Salary',
        ),
        migrations.AddField(
            model_name='employee',
            name='Salary',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
