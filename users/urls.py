from django.urls import path, include
from users import views

app_name = "users"


urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.SignupUserView.as_view(), name="signup"),
    # path("logout/", views.LogOutUserView.as_view(), name="logout")
]
