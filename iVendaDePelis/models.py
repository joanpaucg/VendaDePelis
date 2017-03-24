from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    title = models.TextField(max_length=20)
    year = models.DateField(max_length=20)
    duration = models.IntegerField(max_length=3)
    genre = models.TextField(max_length=20)
    plot = models.TextField()
    price = models.DecimalField('$', max_digits = 4, decimal_places = 2,default=18)
    client=models.ManyToManyField(User)

class Actor(models.Model):
    name = models.TextField(max_length=30)
    birthday = models.DateField("birthday")
    country = models.TextField(blank=True,null=True)
    biography = models.TextField(blank=True,null=True)
    films=models.ManyToManyField(Film)


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),\
    (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank = False, default = 3, choices = RATING_CHOICES)
    opinion = models.TextField()
    user=models.ForeignKey(User)
    film=models.ForeignKey(Film)
class FavouriteList(models.Model):
    user=models.ForeignKey(User)
    films=models.ManyToManyField(Film)

