# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 16:04
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor', '0014_authinformation_do_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='crash',
            name='owner',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]