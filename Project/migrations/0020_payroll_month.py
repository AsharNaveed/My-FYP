# Generated by Django 3.1.dev20200305084444 on 2020-04-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0019_auto_20200423_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='Month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=100, null=True),
        ),
    ]
