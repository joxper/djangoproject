# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20170725_1058'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='Item',
        ),
    ]
