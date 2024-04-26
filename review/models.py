
from django.db import models
from core import models as core_model
import statistics
from django.core.validators import MinValueValidator, MaxValueValidator
from reservations import models as reservation_models


VALIDATOR = [
    MinValueValidator(1),
    MaxValueValidator(5)
]

# Create your models here.


class Review(core_model.TimeStamps):
    """Review Model Definition"""
    REVIEW_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    review = models.TextField(max_length=1000)
    accuracy = models.IntegerField(
        validators=VALIDATOR, choices=REVIEW_CHOICES, default=5)
    communication = models.IntegerField(
        validators=VALIDATOR, choices=REVIEW_CHOICES, default=5)
    clearniness = models.IntegerField(
        validators=VALIDATOR, choices=REVIEW_CHOICES, default=5)
    location = models.IntegerField(
        validators=VALIDATOR, choices=REVIEW_CHOICES, default=5)
    check_in = models.IntegerField(
        validators=VALIDATOR, choices=REVIEW_CHOICES, default=5)
    value = models.IntegerField(
        validators=VALIDATOR, choices=REVIEW_CHOICES, default=5)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name='review')

    def __str__(self) -> str:
        return self.review

    def averge_review(self):
        values = [self.accuracy, self.communication,
                  self.clearniness, self.location, self.check_in, self.value]
        return round((sum(values)/len(values)), 2)
