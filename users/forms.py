from users import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models  # Assuming your models are in a file named models.py


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'


class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "username",
                  "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
