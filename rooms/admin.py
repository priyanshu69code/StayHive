from django.contrib import admin
from rooms.models import Room, HouseRule, Amenities, Facility, RoomType
# Register your models here.


admin.site.register(Room)
admin.site.register(HouseRule)
admin.site.register(Facility)
admin.site.register(Amenities)
admin.site.register(RoomType)
