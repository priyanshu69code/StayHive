from django.urls import path, include
from rooms import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.RoomDetailView.as_view(), name="detail"),
    path("search/", views.RoomSearchView.as_view(), name='search'),
    path("create/", views.CreateRoomView.as_view(), name="create"),
    path("<int:pk>/edit", views.RoomUpdateView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.RoomPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/adds", views.AddPhotoView.as_view(), name="adds-photo"),
    path('<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room-delete'),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhoto.as_view(),
        name="edit-photo",
    ),
    path("switch-hosting/", views.switch_hosting, name="switch-hosting"),
]
