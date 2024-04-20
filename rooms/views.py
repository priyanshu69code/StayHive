from django.shortcuts import redirect
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import Room
from django.shortcuts import render
from rooms.models import Room, RoomPhotos
from django.views.generic import DetailView, UpdateView, FormView
from .forms import RoomsFilter, CreatePhotoForm
from rooms import mixin
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class RoomDetailView(DetailView):
    model = Room
    template_name = "rooms/room_detail.html"


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


class RoomUpdateView(mixin.BelongsOnlyView, UpdateView):
    template_name = "rooms/room_edit.html"
    model = Room
    fields = [
        "name",
        "description",
        "country",
        "city",
        "address",
        "price_per_night",
        "max_guests",
        "is_available",
        "beds",
        "bedrooms",
        "baths",
        "checkin",
        "checkout",
        "room_type",
        "facilities",
        "amenities",
        "house_rules"
    ]


class RoomPhotosView(mixin.BelongsOnlyView, DetailView):
    model = Room
    template_name = "rooms/room_photos.html"


def delete_photo(request, room_pk, photo_pk):
    user = request.user
    try:
        room = Room.objects.get(pk=room_pk)
        if room.host.pk != user.pk:
            messages.error(
                request, 'You do not have permission to delete this image')
            return redirect('core:home')
        else:
            img = RoomPhotos.objects.get(pk=photo_pk)
            img.delete()
            messages.success(request, 'Image deleted successfully!')
            return redirect("rooms:photos", pk=room_pk)
    except (Room.DoesNotExist, RoomPhotos.DoesNotExist):
        messages.error(request, 'Invalid action')
        return redirect('core:home')


class EditPhoto(LoginRequiredMixin, UpdateView):
    model = RoomPhotos
    template_name = "rooms/photo_edit.html"
    fields = ["caption",]
    pk_url_kwarg = "photo_pk"

    def get_object(self, queryset=None):
        photo = super().get_object(queryset)
        room_pk = self.kwargs.get('room_pk')
        room = Room.objects.get(pk=room_pk)
        if (room.host.pk != self.request.user.pk) and (photo.room.pk != room_pk):
            messages.error(self.request, 'Invalid action')
            return redirect('core:home')
        return photo

    def get_success_url(self):
        room_pk = self.kwargs.get("room_pk")
        return reverse("rooms:photos", kwargs={"pk": room_pk})


class AddPhotoView(LoginRequiredMixin, FormView):
    model = RoomPhotos
    template_name = "rooms/photo_create.html"
    form_class = CreatePhotoForm

    def form_valid(self, form):
        room_pk = self.kwargs.get("pk")
        room = Room.objects.get(pk=room_pk)
        if (room.host.pk != self.request.user.pk):
            messages.error(self.request, 'Invalid action')
            return redirect('core:home')
        request = self.request
        form.save(room_pk, request=request)
        return redirect(reverse("rooms:photos", kwargs={"pk": room_pk}))
