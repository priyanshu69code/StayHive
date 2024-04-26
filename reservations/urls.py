from django.urls import path
from . import views


app_name = "reservations"

urlpatterns = [
    path(
        "extra-details/<int:room>/<int:year>-<int:month>-<int:day>",
        views.reservationExtraDetails,
        name="extra-details",
    ),
    path(
        "create/<int:room>/<int:year>-<int:month>-<int:day>-<int:stays>-<int:guests>",
        views.create,
        name="create",
    ),
    path("<int:pk>/", views.ReservationDetailView.as_view(), name="detail"),
    path("<int:pk>/<str:verb>", views.edit_reservation, name="edit"),
]
