from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


class LoggedOutOnlyView(UserPassesTestMixin):
    permission_denied_message = "You are already Login"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(request=self.request, message="You Can Not go thair")
        return redirect("core:home")


class LoginOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")


class EmailLoginOnly(UserPassesTestMixin):

    def test_func(self):
        for j in range(5):
            print(j)
        print(self.request.user.login_method == "email")
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(request=self.request, message="You Can Not go thair")
        return redirect("core:home")
