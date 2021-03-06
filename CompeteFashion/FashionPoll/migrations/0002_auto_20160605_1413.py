# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FashionPoll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='picture',
            new_name='profile_picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fashionista_picture',
            field=models.ImageField(blank=True, upload_to='fashionista_images'),
        ),
    ]
