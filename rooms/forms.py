from typing import Any
from django import forms
from django_countries.fields import CountryField
from . import models
from django.contrib import messages


class RoomsFilter(forms.Form):
    city = forms.CharField(label="City", required=False)
    country = CountryField(default="IN").formfield(required=False)
    host_superhost = forms.BooleanField(label="Superhost", required=False)
    room_type = forms.ModelChoiceField(
        queryset=models.RoomType.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    min_price = forms.IntegerField(
        label='Min price ($)', required=False,
        widget=forms.TextInput(attrs={'placeholder': '5'})
    )
    max_price = forms.IntegerField(
        label='Max price ($)', required=False,
        widget=forms.TextInput(attrs={'placeholder': '1000'})
    )
    min_beds = forms.IntegerField(
        label='Min Beds', required=False,
        widget=forms.TextInput(attrs={'placeholder': '2'})
    )
    bedrooms = forms.IntegerField(
        label='Number of Bed Rooms', required=False,
        widget=forms.TextInput(attrs={'placeholder': '2'})
    )
    baths = forms.IntegerField(
        label='Number of Bath Rooms', required=False,
        widget=forms.TextInput(attrs={'placeholder': '2'})
    )
    facilities = forms.ModelChoiceField(queryset=models.Facility.objects.all(
    ), required=False, widget=forms.CheckboxSelectMultiple)
    amenities = forms.ModelChoiceField(queryset=models.Amenities.objects.all(
    ), required=False, widget=forms.CheckboxSelectMultiple)


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.RoomPhotos
        fields = ("caption", "img")

    def save(self, room_pk, request):
        room = models.Room.objects.get(pk=room_pk)
        photos = super().save(commit=False)
        photos.room = room
        messages.success(request, "Photo Uploaded Succss Fully")
        photos.save()
