# Generated by Django 2.1.1 on 2018-11-13 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0013_auto_20181113_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavebalance',
            name='Emp_No_LeaveBal',
        ),
        migrations.DeleteModel(
            name='LeaveBalance',
        ),
    ]
