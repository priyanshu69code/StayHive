from django import template
from reservations.models import BookedDay
from datetime import datetime

register = template.Library()


@register.simple_tag
def is_booked(room, day):
    if day.number == 0:
        return False
    try:
        date = datetime(day.year, day.month, day.number)
        booking = BookedDay.objects.get(day=date, reservation__room=room)
        return True
    except BookedDay.DoesNotExist:
        return False
