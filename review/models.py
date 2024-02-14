
from django.db import models
from core import models as core_model
import statistics

# Create your models here.


class Review(core_model.TimeStamps):
    review = models.CharField(max_length=1000)
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    clearniness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name='review')

    def __str__(self) -> str:
        return self.review

    def averge_review(self):
        values = [self.accuracy, self.communication,
                  self.clearniness, self.location, self.check_in, self.value]
        return round((sum(values)/len(values)), 2)
