from django.urls import path, include
from core import views
app_name = "core"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
