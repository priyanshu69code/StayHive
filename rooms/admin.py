from django.contrib import admin
from rooms.models import Room, HouseRule, Amenities, Facility, RoomType
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "country",
                    "city",
                    "address",
                    "max_guests",
                    "is_available",
                    "beds",
                    "host")
    search_fields = ["country", "name", "host__username"]
    list_filter = ["is_available", "country", "city"]

    filter_horizontal = ["house_rules", "amenities", "facilities"]


admin.site.register(Room, RoomAdmin)
admin.site.register(HouseRule)
admin.site.register(Facility)
admin.site.register(Amenities)
admin.site.register(RoomType)
