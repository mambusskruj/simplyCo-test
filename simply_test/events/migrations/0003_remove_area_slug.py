# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-07 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160807_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='slug',
        ),
    ]
