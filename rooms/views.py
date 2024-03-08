from django.shortcuts import render
from rooms.models import Room
from django.views.generic import DetailView
from django_countries import countries
from rooms.models import RoomType
# Create your views here.


class HomeView(DetailView):
    model = Room
    template_name = "rooms/detail.html"


def search(request):
    city = request.GET.get('city', '').capitalize()
    roomtype = RoomType.objects.all()
    context = {"city": city,
               "countries": countries,
               "roomtypes": roomtype}
    return render(request, 'rooms/search.html', context)
