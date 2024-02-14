from django.contrib import admin
from rooms.models import Room, HouseRule, Amenities, Facility, RoomType, RoomPhotos
from django.utils.html import mark_safe
# Register your models here.


class PhotoInline(admin.TabularInline):
    model = RoomPhotos
    extra = 1
    verbose_name = "DP"


class RoomAdmin(admin.ModelAdmin):
    # Fields to show in the main view of the object
    inlines = (PhotoInline,)
    fieldsets = [
        ('Basic Information', {'fields': [
         'name', 'description', "address", 'city', 'country', "price_per_night"]}),
        ("Spaces", {"fields": ["is_available",
         "beds", "bedrooms", "baths", "max_guests"]}),
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
                    "count_rules",
                    "count_photos",
                    "room_avg_rev")
    search_fields = ["country", "name", "host__username"]
    list_filter = ["is_available", "country", "city"]

    raw_id_fields = ("host",)

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

    def count_photos(self, obj):
        return len(obj.photos.all())
    count_photos.short_description = "Number of photos"


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img  src='{obj.img.url}' width='50px' />")


admin.site.register(Room, RoomAdmin)
admin.site.register(HouseRule)
admin.site.register(Facility)
admin.site.register(Amenities)
admin.site.register(RoomType)
admin.site.register(RoomPhotos, PhotoAdmin)
