from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Film, FavouriteList, Actor,Review
from views import LoginRequiredCheckIsOwnerUpdateView,review,FilmDetail,ActorDetail,register,ReviewCreate, FavouriteListView, FavouriteListCreate,LoginRequiredCheckIsOwnerDeleteView
from forms import ReviewEditForm
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
    url(r'^favouritelists/(?P<pk>\d+)/$',
            FavouriteListView.as_view(),
            name="favourite_list_detail"
        ),
    url(r'^favouritelists/create/$',
            FavouriteListCreate.as_view(),
            name="favouritelist_create"

        ),
    # Delete LlistaDeFavorits
    url(r'^favouritelists/(?P<pk>\d+)/delete/$',
       LoginRequiredCheckIsOwnerDeleteView.as_view(model=FavouriteList),
       name='favouritelist_delete'),

]