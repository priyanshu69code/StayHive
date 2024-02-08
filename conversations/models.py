from django.db import models
import core.models as core_models

# Create your models here.


class Converstions(core_models.TimeStamps):
    participants = models.ManyToManyField(
        "users.User", related_name="conversations")

    def __str__(self) -> str:
        return str(self.created_at)


class Message(core_models.TimeStamps):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True)
    converstions = models.ForeignKey(Converstions, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} says: {self.text[:50]}"
