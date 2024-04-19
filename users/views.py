import os
from django.forms import BaseModelForm
from django.forms.forms import BaseForm
import requests
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from users import forms
from users import models
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class LoginUserView(mixin.LoggedOutOnlyView, LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    form_class = forms.LoginForm

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        else:
            return reverse("core:home")


class SignupUserView(mixin.LoggedOutOnlyView, CreateView):
    form_class = forms.SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        user.verify_email()  # Call the verify_email method
        return response


@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, "See You Latter")
    return redirect(reverse("core:home"))


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
    except models.User.DoesNotExist:
        pass
    return redirect("core:home")


def github_login(request):
    gh_cid = os.environ.get("GH_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(f"https://github.com/login/oauth/authorize?client_id={gh_cid}&redirect_uri={redirect_uri}&scope=read:user")


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GH_ID")
        client_secret = os.environ.get("GH_SECRET")
        code = request.GET.get("code", None)
        if code is not None:
            token_request = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={
                    client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
            )
            token_json = token_request.json()
            error = token_json.get("error", None)
            if error is not None:
                raise GithubException("Can't get access token")
            else:
                access_token = token_json.get("access_token")
                profile_request = requests.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"token {access_token}",
                        "Accept": "application/json",
                    },
                )
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")
                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException(
                                f"Please log in with: {user.login_method}"
                            )
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(
                            email=email,
                            first_name=name,
                            username=email,
                            bio=bio,
                            login_method=models.User.LOGIN_GITHUB,
                            email_verified=True,
                        )
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    messages.success(request, f"Welcome back {
                                     user.first_name}")
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException("Can't get your profile")
        else:
            raise GithubException("Can't get code")
    except GithubException as e:
        messages.error(request, e)
        return redirect(reverse("users:login"))


class UserDetailView(DetailView):
    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(mixin.LoginOnlyView, SuccessMessageMixin, UpdateView,):
    template_name = "users/update_profile.html"
    success_message = "Profile Updated Succesfully"
    fields = (
        "avatar",
        "first_name",
        "last_name",
        "gender",
        "bio",
        "language",
    )

    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        updateform = super().get_form(form_class)
        updateform.fields['first_name'].widget.attrs['placeholder'] = 'Enter your First name'
        updateform.fields['last_name'].widget.attrs['placeholder'] = 'Enter your Last name'
        updateform.fields['gender'].widget.attrs['placeholder'] = 'Select Your Gender name'
        updateform.fields['bio'].widget.attrs['placeholder'] = 'Write a bio'
        return updateform


class UpdatePasswordView(mixin.EmailLoginOnly, SuccessMessageMixin, PasswordChangeView):
    template_name = "users/update_password.html"
    success_message = "Password changed  successfully!"
    success_url = reverse_lazy("users:update")

    def get_form(self, form_class=None):
        password_update = super().get_form(form_class)
        password_update.fields['old_password'].widget.attrs['placeholder'] = 'Enter Old Password'
        password_update.fields['new_password1'].widget.attrs['placeholder'] = 'Enter New Password'
        password_update.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        return password_update
