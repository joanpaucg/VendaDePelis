# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iVendaDePelis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='price',
            field=models.DecimalField(decimal_places=2, default=18, max_digits=4, verbose_name='$'),
        ),
    ]
