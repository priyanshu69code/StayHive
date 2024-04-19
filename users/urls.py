from django.urls import path, include
from users import views

app_name = "users"


urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.SignupUserView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="verify"),
    # path("logout/", views.LogOutUserView.as_view(), name="logout"),
    path("github/login", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("<int:pk>", views.UserDetailView.as_view(), name="profile"),
    path("update", views.UpdateProfileView.as_view(), name="update"),
    path("update/password", views.UpdatePasswordView.as_view(),
         name="update-password")
]
