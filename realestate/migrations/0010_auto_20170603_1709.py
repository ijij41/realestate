# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0009_auto_20170603_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='dongcode',
            field=models.BigIntegerField(db_column='dongCode', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='guguncode',
            field=models.IntegerField(db_column='gugunCode', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='sidocode',
            field=models.IntegerField(db_column='sidoCode', default=1),
            preserve_default=False,
        ),
    ]
