from django.db import models
import core.models as core_model
from django.utils import timezone
from core import managers
import datetime
# Create your models here.
NOW = timezone.now().date()


class BookedDay(core_model.TimeStamps):
    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day)


class Reservation(core_model.TimeStamps):
    """Reservation Model Definition"""
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    reviewed = models.BooleanField(default=False)
    number_of_guests = models.IntegerField()

    def is_progress(self):
        return NOW > self.check_in and NOW < self.check_out
    is_progress.boolean = True

    def is_finished(self):
        # return NOW > self.check_out
        if is_finished := self.status == self.STATUS_CONFIRMED and NOW > self.check_out:
            BookedDay.objects.filter(reservation=self).delete()
        return True
    is_finished.boolean = True

    def change_reviewed(self):
        self.reviewed = True
        self.save()

    def is_reviewed(self):
        return self.reviewed

    def save(self, *args, **kwargs):
        if self.pk is None:
            start = self.check_in
            end = self.check_out
            difference = end - start
            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()
            if not existing_booked_day:
                super().save(*args, **kwargs)
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    BookedDay.objects.create(day=day, reservation=self)
                return
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
