from django.conf.urls import url,include
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Film, FavouriteList, Actor,Review
from views import *
from forms import ReviewEditForm,FavouriteListForm
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^accounts/register/$', register, name='register'),
    url(r'^films/$',
        ListView.as_view(
            queryset=Film.objects.all(),
            context_object_name='latest_film_list',
            template_name='VendaDePelis/film_list.html'),
            name='film_list'),

    url(r'^films/(?P<pk>\d+)/$',
            FilmDetail.as_view(),
            name='film_detail'),
    url(r'^films/(?P<pk>\d+)/reviews/create/$',
            review,
            name='review_create'),
    url(r'^films/(?P<pkr>\d+)/reviews/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(model=Review,form_class=ReviewEditForm),
        name='review_edit'),
    url(r'^films/(?P<pkr>\d+)/reviews/(?P<pk>\d+)/delete/$',
        LoginRequiredCheckIsOwnerDeleteView.as_view(model=Review,
                                                    template_name='VendaDePelis/delete_object.html'
                                                     ),
        name='review_delete'),
    url(r'^actors/(?P<pk>\d+)/$',
            ActorDetail.as_view(),
            name='actor_detail'),
    url(r'^favouritelists/$',
        ListView.as_view(
            queryset=FavouriteList.objects.all(),
            context_object_name='latest_favourite_lists',
            template_name='VendaDePelis/favouritelist_list.html'),
            name='favouritelist'),
    url(r'^favouritelists/(?P<pk>\d+)/$',
            FavouriteListView.as_view(),
            name="favouritelist_detail"
        ),
    url(r'^favouritelists/create/$',
            FavouriteListCreate.as_view(),
            name="favouritelist_create"

        ),
    # Delete LlistaDeFavorits
    url(r'^favouritelists/(?P<pk>\d+)/delete/$',
       LoginRequiredCheckIsOwnerDeleteView.as_view(model=FavouriteList),
       name='favouritelist_delete'),
    url(r'^favouritelists/(?P<pk>\d+)/edit/$',
       LoginRequiredCheckIsOwnerUpdateView.as_view(model=FavouriteList,form_class=FavouriteListForm),
       name='favouritelist_edit'),

]

### RESTful API url ###
urlpatterns+=[
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/films/$',APIFilmList.as_view(),name='film-list'),
    url(r'^api/films/(?P<pk>\d+)/$',APIFilmDetail.as_view(),name='film-detail'),
    url(r'^api/actors/$',APIActorList.as_view(),name='actor-detail'),
    url(r'^api/actors/(?P<pk>\d+)/$',APIActorDetail.as_view(),name='actor-detail'),
    url(r'^api/filmreviews/(?P<pk>\d+)/$', APIFilmReviewDetail.as_view(),name='filmreview-detail'),

]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])