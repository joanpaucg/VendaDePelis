from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from models import Film, FavouriteList
from models import Review
# Create your views here.
class FilmDetail(DetailView):
    model = Film
    template_name = "VendaDePelis/film_detail.html"

    def get_context_data(self, **kwargs):
        context = super(FilmDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = Review.RATING_CHOICES
        return context

class ReviewCreate(CreateView):
    model = Review
    template_name = "iVendaDePelis/templates/VendaDePelis/review_form.html"
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreate, self).form_valid(form)

class FavouriteListView(DetailView):
    model = FavouriteList
    template_name = "iVendaDePelis/templates/VendaDePelis/favourite_list_detail.html"

class FavouriteListCreate(CreateView):
    model = FavouriteList
    template_name = "iVendaDePelis/templates/VendaDePelis/favourite_list_create.html"
    form_class = FavouriteListForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FavouriteListCreate, self).form_valid(form)