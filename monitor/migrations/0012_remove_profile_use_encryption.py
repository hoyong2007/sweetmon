# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_auto_20170702_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='use_encryption',
        ),
    ]
