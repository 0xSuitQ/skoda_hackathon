# Generated by Django 5.1.2 on 2024-10-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0004_remove_drivingdata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drivingdata',
            name='user_number_1',
        ),
        migrations.RemoveField(
            model_name='drivingdata',
            name='user_number_2',
        ),
        migrations.RemoveField(
            model_name='drivingdata',
            name='user_number_3',
        ),
        migrations.RemoveField(
            model_name='drivingdata',
            name='user_number_4',
        ),
    ]
