from django.views.generic import ListView
from .models import Room
from django.shortcuts import render
from rooms.models import Room
from django.views.generic import DetailView, ListView
from .forms import RoomsFilter


class HomeView(DetailView):
    model = Room
    template_name = "rooms/detail.html"


class RoomSearchView(ListView):
    template_name = 'rooms/search.html'
    form_class = RoomsFilter
    model = Room
    context_object_name = 'rooms'

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.GET.get("country")
        city = self.request.GET.get("city")
        room_type = self.request.GET.get("room_type")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        min_beds = self.request.GET.get("min_beds")
        bedrooms = self.request.GET.get("bedrooms")
        baths = self.request.GET.get("baths")
        facilities = self.request.GET.getlist("facilities")
        amenities = self.request.GET.getlist("amenities")

        if country:
            queryset = queryset.filter(country=country)
        if city:
            queryset = queryset.filter(city__icontains=city)
        if room_type:
            queryset = queryset.filter(room_type=room_type)
        if min_price:
            queryset = queryset.filter(price_per_night__gte=min_price)
        if max_price:
            queryset = queryset.filter(price_per_night__lte=max_price)
        if min_beds:
            queryset = queryset.filter(beds__gte=min_beds)
        if bedrooms:
            queryset = queryset.filter(bedrooms=bedrooms)
        if baths:
            queryset = queryset.filter(baths=baths)
        if facilities:
            queryset = queryset.filter(facilities__in=facilities)
        if amenities:
            queryset = queryset.filter(amenities__in=amenities)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RoomsFilter(self.request.GET)
        return context
