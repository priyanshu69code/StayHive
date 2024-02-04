from django.db import models

# Create your models here.


class TimeStamps(models.Model):
    """This is Time Stamp Model"""
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
