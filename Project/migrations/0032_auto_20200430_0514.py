# Generated by Django 3.1.dev20200305084444 on 2020-04-30 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project', '0031_auto_20200430_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='Attendance_No',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Early_Going',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_user_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]