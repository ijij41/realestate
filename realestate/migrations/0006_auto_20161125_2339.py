# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_auto_20161125_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='deal_date',
            field=models.DateField(db_column='DEAL_DATA'),
        ),
    ]
