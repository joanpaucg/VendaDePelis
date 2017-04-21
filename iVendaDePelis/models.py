from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse






class Film(models.Model):
    TYPES= (('Comedy', 'Comedy'), ('Action', 'Action'), ('Drama', 'Drama'), ('Terror', 'Terror'),
             ('Fantasy', 'Fantasy'), ('Thriller', 'Thriller'), ('Adventure', 'Adventure'),
             ('ScienceFiction', 'ScienceFiction'),
             ('Western', 'Western'))
    title = models.TextField(max_length=20)
    year = models.DateField(max_length=20)
    duration = models.IntegerField(blank=True,null=True)
    genre = models.CharField(max_length=20,choices=TYPES,unique=True)
    plot = models.TextField(blank=True,null=True)
    price = models.DecimalField('Euro amount', max_digits = 4, decimal_places = 2,default=18)
    clients=models.ManyToManyField(User,related_name='films')
    def __unicode__(self):
        return u"%s"%self.title
    def get_absolute_url(self):
        return reverse('iVendaDePelis:film_detail',kwargs={'pk':self.pk})

class Actor(models.Model):
    name = models.TextField(max_length=30)
    birthday = models.DateField("birthday",blank=True,null=True)
    country = models.TextField(blank=True,null=True)
    biography = models.TextField(blank=True,null=True)
    films=models.ManyToManyField(Film,related_name='actors')
    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('iVendaDePelis:actor_detail',kwargs={'pk':self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),\
    (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank = False, default = 3, choices = RATING_CHOICES)
    opinion = models.TextField(blank=True,null=True)
    user=models.ForeignKey(User)
    film=models.ForeignKey(Film,related_name='reviews')


class FavouriteList(models.Model):
    name=models.TextField(max_length=30,default='FavouriteList')
    creation_date=models.DateField('Creation Date',auto_now_add=True)
    user=models.ForeignKey(User,related_name='mylists')
    films=models.ManyToManyField(Film)
    def __unicode__(self):
        return u"%s" % self.name
