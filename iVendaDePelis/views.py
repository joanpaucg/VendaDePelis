from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from models import Film, FavouriteList,Actor
from models import Review
from iVendaDePelis.forms import UserForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


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
    #form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreate, self).form_valid(form)

class FavouriteListView(DetailView):
    model = FavouriteList
    template_name = "iVendaDePelis/templates/VendaDePelis/favourite_list_detail.html"

class FavouriteListCreate(CreateView):
    model = FavouriteList
    template_name = "iVendaDePelis/templates/VendaDePelis/favourite_list_create.html"
    #form_class = FavouriteListForm

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
