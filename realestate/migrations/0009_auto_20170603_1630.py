# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0008_deal_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='dongcode',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='guguncode',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='sidocode',
        ),
    ]
