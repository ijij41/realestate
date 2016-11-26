# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('si_code', models.IntegerField()),
                ('si_name', models.CharField(max_length=20)),
                ('gu_code', models.IntegerField()),
                ('gu_name', models.CharField(max_length=20)),
                ('dong_code', models.BigIntegerField()),
                ('dong_name', models.CharField(max_length=20)),
            ],
        ),
    ]