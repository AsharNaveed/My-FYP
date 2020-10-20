# Generated by Django 3.1.dev20200305084444 on 2020-04-23 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0023_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Any_Leave', models.CharField(choices=[('One', 'One'), ('Two', 'Two'), ('Three', 'Three'), ('Four', 'Four'), ('None', 'None')], max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='Any_Leave',
        ),
        migrations.AddField(
            model_name='attendance',
            name='leave',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project.Leave'),
        ),
    ]
