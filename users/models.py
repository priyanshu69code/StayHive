from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """This is Custom user model for StayHive"""
    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    gender = models.ForeignKey(
        'Gender', on_delete=models.SET_NULL, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    language = models.ForeignKey(
        "Language", on_delete=models.SET_NULL, null=True, blank=True,)
    country = models.ForeignKey(
        "Country", on_delete=models.SET_NULL, null=True, blank=True)
    superhost = models.BooleanField(default=False)


class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
