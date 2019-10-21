# Generated by Django 2.2.3 on 2019-10-21 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='misc',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stay',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='transit',
            name='trip',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
        migrations.RemoveField(
            model_name='tripcomment',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='tripcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tripuser',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='tripuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usersetting',
            name='user',
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='Misc',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Stay',
        ),
        migrations.DeleteModel(
            name='Transit',
        ),
        migrations.DeleteModel(
            name='TripComment',
        ),
        migrations.DeleteModel(
            name='TripUser',
        ),
        migrations.DeleteModel(
            name='UserSetting',
        ),
    ]
