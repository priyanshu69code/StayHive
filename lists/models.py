from django.db import models
import core.models as core_models

# Create your models here.


class List(core_models.TimeStamps):
    name = models.CharField(max_length=80)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self) -> str:
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"
