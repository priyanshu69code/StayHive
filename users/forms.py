from users import models
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "username", "email", "password1",
                  "password2")
