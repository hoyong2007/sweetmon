# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_crash_is_encrypted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authinformation',
            name='owner',
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram_number',
            field=models.IntegerField(blank=True, help_text="To get your chat_id, Add '@get_id_bot' and send '/my_id'", null=True),
        ),
        migrations.DeleteModel(
            name='AuthInformation',
        ),
    ]
