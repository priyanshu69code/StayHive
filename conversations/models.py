from django.db import models
import core.models as core_models

# Create your models here.


class Converstions(core_models.TimeStamps):
    participants = models.ManyToManyField(
        "users.User", related_name="conversations")

    def __str__(self) -> str:
        username = [user for user in self.participants.all()]
        return f"Conversation between {', '.join([str(u) for u in username])}"

    def count_messages(self) -> int:
        return self.message.count()


class Message(core_models.TimeStamps):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True)
    converstions = models.ForeignKey(
        Converstions, on_delete=models.CASCADE, related_name="message")

    def __str__(self) -> str:
        return f"{self.user} says: {self.text[:50]}"
