# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 08:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FashionPoll', '0002_auto_20160605_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fashionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fashionista_picture', models.ImageField(blank=True, upload_to='fashionista_images')),
                ('title', models.CharField(max_length=250)),
                ('likes', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='fashionista_picture',
        ),
    ]