# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FashionPoll', '0003_auto_20160606_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL)),
                ('unliked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unliked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fashionista',
            name='rating',
            field=models.DecimalField(db_index=True, decimal_places=4, default=1000.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='fashionista',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fashionista',
            name='fashionista_picture',
            field=models.ImageField(upload_to='fashionista_images'),
        ),
        migrations.AlterIndexTogether(
            name='order',
            index_together=set([('liker', 'created_at')]),
        ),
    ]
