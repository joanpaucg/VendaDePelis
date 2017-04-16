# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 12:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iVendaDePelis', '0007_auto_20170416_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='favouritelist',
            name='creation_date',
            field=models.DateField(default=datetime.date(2017, 4, 16), verbose_name='Creation Date'),
        ),
        migrations.AddField(
            model_name='favouritelist',
            name='name',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
