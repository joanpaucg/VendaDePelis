# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iVendaDePelis', '0008_auto_20170416_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritelist',
            name='name',
            field=models.TextField(default='FavouriteList', max_length=30),
        ),
    ]
