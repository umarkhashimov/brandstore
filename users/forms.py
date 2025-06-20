from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsersModel

class RegistrationForm(UserCreationForm):

    class Meta:
        model = UsersModel
        fields = ['first_name', 'last_name', 'username',  'password1', 'password2' ]