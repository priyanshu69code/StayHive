from django.db import models
from django_countries.fields import CountryField
import core.models as CoreModel
from users.models import User as Host
# Create your models here.


class RoomType(CoreModel.AbstractThings):
    pass


class Facility(CoreModel.AbstractThings):
    pass


class Amenities(CoreModel.AbstractThings):
    pass


class HouseRule(CoreModel.AbstractThings):
    pass


class Room(CoreModel.TimeStamps):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=200,  null=True, choices=CountryField(
        # https://stackoverflow.com/questions/77667419/problem-after-upgrading-to-django-5-0-attributeerror-blankchoiceiterator-obj#:~:text=The%20error%20you're%20encountering,parameter%20in%20ChoiceField%20has%20changed.
    ).choices + [('', 'Select Country')])
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    max_guests = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    checkin = models.TimeField()
    checkout = models.TimeField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE, null=True)
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True)
    facilities = models.ManyToManyField(Facility)
    amenities = models.ManyToManyField(Amenities)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
