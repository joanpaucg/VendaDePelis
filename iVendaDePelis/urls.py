from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Film, FavouriteList, Actor
from views import FilmDetail,ActorDetail,register,ReviewCreate, FavouriteListView, FavouriteListCreate

urlpatterns = [
    url(r'^accounts/register/$', register, name='register'),
    url(r'^films/$',
        ListView.as_view(
            queryset=Film.objects.all(),
            context_object_name='latest_film_list',
            template_name='VendaDePelis/film_list.html'),
            name='film_list'),

    url(r'^films/film/(?P<pk>\d+)/$',
            FilmDetail.as_view(),
            name='film_detail'),
    url(r'^actors/(?P<pk>\d+)/$',
            ActorDetail.as_view(),
            name='actor_detail'),
]