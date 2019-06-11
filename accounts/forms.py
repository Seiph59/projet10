""" File used to create and personnalize the UserRegisterForm """
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """ Inherited from UserCreationForm
    to personnalize the registration form """
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, label="Prénom")
    last_name = forms.CharField(max_length=30, label="Nom")

    class Meta:
        """ Define the order of Fields """
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2']
