# Generated by Django 2.2.3 on 2019-10-24 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_scheduledattendee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledattendee',
            name='duration',
            field=models.DurationField(blank=True, default=None, null=True, verbose_name='Duration'),
        ),
    ]
