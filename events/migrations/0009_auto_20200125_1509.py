# Generated by Django 2.2.3 on 2020-01-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20200125_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='signup_end_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Sign-up End Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_start_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Sign-up Start Date'),
        ),
    ]
