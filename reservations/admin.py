from django.contrib import admin
from reservations.models import Reservation, BookedDay

# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest', 'room', 'check_in',
                    'check_out', "is_progress", "is_finished", "status")
    search_fields = ("guest", "room")
    list_filter = ("status",)


class BookedDayAdmin(admin.ModelAdmin):
    list_display = ('day', 'reservation')
    search_fields = ("day", "reservation")
    list_filter = ("day", "reservation")


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(BookedDay, BookedDayAdmin)
