from django.db import models
import core.models as core_model
# Create your models here.


class Status(core_model.AbstractThings):
    pass


class Reservation(core_model.TimeStamps):
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.ForeignKey(
        Status, null=True, blank=True, on_delete=models.SET_NULL)
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
