from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Film, FavouriteList, Actor
from forms import ReviewForm, FavouriteListForm
from views import FilmDetail, ReviewCreate, FavouriteListView, FavouriteListCreate

urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Films.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
            context_object_name='latest_film_list',
            template_name='VendaDePelis/film_detail.html'),
        name='film_list'),

    url(r'^films/(?P<pk>\d+)/$',
            FilmDetail.as_view(),
            name='film_detail'),
]