# Generated by Django 3.1.dev20200305084444 on 2020-05-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0035_auto_20200506_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Time_In',
            field=models.CharField(choices=[('AM', 'am'), ('PM', 'pm')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Time_Out',
            field=models.CharField(max_length=100, null=True),
        ),
    ]