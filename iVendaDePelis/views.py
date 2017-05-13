from django.shortcuts import reverse, render_to_response,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView,UpdateView
from models import Film, FavouriteList,Actor,Review
from iVendaDePelis.forms import UserForm,FavouriteListForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
# Create your views here.
class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj
class LoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    template_name = 'VendaDePelis/delete_object.html'
    success_url = "/ivendadepelis/films"
class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'VendaDePelis/form.html'
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
    #form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreate, self).form_valid(form)

class FavouriteListView(DetailView):
    model = FavouriteList
    template_name = "VendaDePelis/favourite_list_detail.html"

class FavouriteListCreate(CreateView):
    model = FavouriteList
    template_name = "VendaDePelis/form.html"
    form_class = FavouriteListForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FavouriteListCreate, self).form_valid(form)
class ActorDetail(DetailView):
    model = Actor
    template_name = "VendaDePelis/actor_detail.html"

@csrf_exempt
def register(request):
    context = RequestContext(request)
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)


        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.


            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
        'registration/register.html',
        {'user_form': user_form,'registered': registered},
        context)
@login_required()
def review(request, pk):
    value=None
    film = get_object_or_404(Film, pk=pk)
    if  request.POST['rating']=="one":
        value=1
    elif request.POST['rating']=="two":
        value=2
    elif request.POST['rating'] == "three":
        value=3
    elif request.POST['rating'] == "four":
        value=4
    elif request.POST['rating'] == "five":
        value=5
    review = Review(
        rating=value,
        opinion=request.POST['opinion'],
        user=request.user,
        film=film)
    review.save()
    return HttpResponseRedirect(reverse('ivendadepelis:film_detail', args=(film.id,)))
