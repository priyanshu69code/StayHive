from django.contrib import admin
from rooms.models import Room, HouseRule, Amenities, Facility, RoomType
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    # Fields to show in the main view of the object
    fieldsets = [
        ('Basic Information', {'fields': [
         'name', 'description', "address", 'city', 'country', "price_per_night"]}),
        ("Spaces", {"fields": ["is_available", "beds", "bedrooms", "baths"]}),
        ("Amenities and Services", {"fields": [
         "room_type", "facilities", "amenities", "house_rules"]}),
        ("Timings", {"fields": ["checkin", "checkout"]}),
        ("Owner", {"fields": ["host"]})
    ]
    list_display = ("name",
                    "country",
                    "city",
                    "address",
                    "max_guests",
                    "is_available",
                    "beds",
                    "host",
                    "count_amenities",
                    "count_facilities",
                    "count_rules")
    search_fields = ["country", "name", "host__username"]
    list_filter = ["is_available", "country", "city"]

    filter_horizontal = ["house_rules", "amenities", "facilities"]

    def count_amenities(self, obj):
        return obj.amenities.count()
    count_amenities.short_description = "Number of amenities"

    def count_facilities(self, obj):
        return obj.facilities.count()
    count_facilities.short_description = "Number of facilities"

    def count_rules(self, obj):
        return obj.house_rules.count()
    count_rules.short_description = "Number of Rules"


admin.site.register(Room, RoomAdmin)
admin.site.register(HouseRule)
admin.site.register(Facility)
admin.site.register(Amenities)
admin.site.register(RoomType)
