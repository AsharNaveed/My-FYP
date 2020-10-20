# Generated by Django 3.1.dev20200305084444 on 2020-04-30 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project', '0032_auto_20200430_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_user_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='empuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Late_Comming',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
    ]