from django.db import models

# Create your models here.


class TimeStamps(models.Model):
    """This is Time Stamp Model"""
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        abstract = True


class AbstractThings(TimeStamps):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class abstract:
        abstract = True

    def __str__(self):
        return self.name
