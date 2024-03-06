from django.urls import path, include
from rooms import views

app_name = "rooms"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
