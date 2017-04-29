from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Film, FavouriteList, Actor
from views import FilmDetail, ReviewCreate, FavouriteListView, FavouriteListCreate

urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Film.objects.all(),
            context_object_name='latest_film_list',
            template_name='VendaDePelis/film_list.html'),
            name='film_list'),

    url(r'^films/(?P<pk>\d+)/$',
            FilmDetail.as_view(),
            name='film_detail'),
]