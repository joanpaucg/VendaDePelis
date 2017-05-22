from django.contrib.auth.models import User
from django import forms
from models import Review,FavouriteList,UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('city', 'country', 'zipCode','stateOrProvince')
class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user','film')
class FavouriteListForm(forms.ModelForm):
    class Meta:
        model = FavouriteList
        exclude = ('user','creation_date')


