from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from users import forms
# Create your views here.


class LoginUserView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        print(next_url)
        if next_url:
            return next_url
        return reverse_lazy("core:home")


class SignupUserView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    # class LogOutUserView(LogoutView):
    #     next_page = redirect(reverse("core:home"))


def logoutUser(request):
    logout(request)
    return redirect(reverse("core:home"))
