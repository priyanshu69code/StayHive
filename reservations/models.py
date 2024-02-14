from django.db import models
import core.models as core_model
from django.utils import timezone
# Create your models here.
NOW = timezone.now().date()


class Status(core_model.AbstractThings):
    pass


class Reservation(core_model.TimeStamps):
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.ForeignKey(
        Status, null=True, blank=True, on_delete=models.SET_NULL)
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def is_progress(self):
        return NOW > self.check_in and NOW < self.check_out
    is_progress.boolean = True

    def is_finished(self):
        return NOW > self.check_out
    is_finished.boolean = True
