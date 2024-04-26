from django.urls import path
from . import views


app_name = "review"

urlpatterns = [
    path("create/<int:reservation_pk>", views.create_review, name="create"),
]
