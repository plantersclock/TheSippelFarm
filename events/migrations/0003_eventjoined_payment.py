# Generated by Django 2.2.3 on 2019-11-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20191024_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventjoined',
            name='payment',
            field=models.CharField(choices=[('Check/Cash', 'Check/Cash'), ('Paypal', 'Paypal')], default='Paypal', max_length=200),
            preserve_default=False,
        ),
    ]
