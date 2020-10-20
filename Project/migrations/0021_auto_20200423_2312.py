# Generated by Django 3.1.dev20200305084444 on 2020-04-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0020_payroll_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Salary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='Basic_Salary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
    ]
