# Generated by Django 2.2.3 on 2019-11-09 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_page_pagecontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='caption_title',
            new_name='content_title',
        ),
        migrations.RenameField(
            model_name='pagecontent',
            old_name='caption_title',
            new_name='content_title',
        ),
        migrations.RemoveField(
            model_name='page',
            name='caption_text',
        ),
        migrations.RemoveField(
            model_name='pagecontent',
            name='caption_text',
        ),
        migrations.AddField(
            model_name='page',
            name='content_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='content_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='order',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='order',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
