# Generated by Django 3.1.dev20200305084444 on 2020-04-17 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_auto_20200418_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='Attendance_ID',
            new_name='Attendance_No',
        ),
    ]
