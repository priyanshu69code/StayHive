from django.shortcuts import render
from rooms.models import Room
from django.views.generic import DetailView
# Create your views here.


class HomeView(DetailView):
    model = Room
    template_name = "rooms/detail.html"
