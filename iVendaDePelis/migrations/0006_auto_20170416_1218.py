# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iVendaDePelis', '0005_auto_20170416_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='client',
        ),
        migrations.AddField(
            model_name='film',
            name='clients',
            field=models.ManyToManyField(related_name='films', to=settings.AUTH_USER_MODEL, verbose_name='list of clients'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='films',
            field=models.ManyToManyField(related_name='actors', to='iVendaDePelis.Film', verbose_name='Actor films'),
        ),
        migrations.AlterField(
            model_name='favouritelist',
            name='films',
            field=models.ManyToManyField(to='iVendaDePelis.Film', verbose_name='list of films'),
        ),
        migrations.AlterField(
            model_name='favouritelist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylists', to=settings.AUTH_USER_MODEL, verbose_name='The related client'),
        ),
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('Action', 'Action'), ('Drama', 'Drama'), ('Terror', 'Terror'), ('Fantasy', 'Fantasy'), ('Thriller', 'Thriller'), ('Adventure', 'Adventure'), ('ScienceFiction', 'ScienceFiction'), ('Western', 'Western')], max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='iVendaDePelis.Film', verbose_name='The related Film'),
        ),
        migrations.AlterField(
            model_name='review',
            name='opinion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='The related client'),
        ),
    ]
