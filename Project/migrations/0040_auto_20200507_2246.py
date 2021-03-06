# Generated by Django 3.1.dev20200305084444 on 2020-05-07 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0039_payroll_no_of_presents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payroll',
            name='Mark_Attendance',
        ),
        migrations.AddField(
            model_name='payroll',
            name='Leave_Utilized',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project.Leave'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='Att_Percentage',
            field=models.CharField(choices=[('100%', '100%'), ('70%', '70%'), ('50%', '50%'), ('Less than 50%', 'Less than 50%')], max_length=50, null=True),
        ),
    ]
