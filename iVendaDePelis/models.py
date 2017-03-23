from __future__ import unicode_literals

from django.db import models

def Film(models.Model):
    film_id = models.IntegerField()
    title = models.TextField()
    year = models.DateField()
    duration = models.IntegerField()
    genre = models.TextField()
    plot = model.TextField()
    price = models.DecimalField('€', max_digits = 2, decimal_places = 2)

def Actor(models.Model):
    name = models.TextField()
    birthday = models.DateField()
    country = models.TextField()
    biography = models.TextField()

def Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),\
    (5, 'five'))
    review_id = models.IntegerField()
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank = False, default = 3, choices = RATING_CHOICES)
    opinion = models.TextField()

def Favourite_list(models.Model):
    
