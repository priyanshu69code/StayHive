from django.urls import path, include
from rooms import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.HomeView.as_view(), name="detail"),
    path("search/", views.RoomSearchView.as_view(), name='search'),
]
