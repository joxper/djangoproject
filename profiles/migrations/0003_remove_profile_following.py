# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170726_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]
