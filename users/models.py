from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse


class User(AbstractUser):
    """This is Custom user model for StayHive"""

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = ((LOGIN_EMAIL, "Email"), (LOGIN_GITHUB,
                     "Github"), (LOGIN_KAKAO, "Kakao"))

    email = models.EmailField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": ("A user with that email already exists."),
        },
    )

    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")
    bio = models.TextField(default="", blank=True)
    gender = models.ForeignKey(
        'Gender', on_delete=models.SET_NULL, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    language = models.ForeignKey(
        "Language", on_delete=models.SET_NULL, null=True, blank=True,)
    country = CountryField(blank=True, null=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)

    def verify_email(self):
        if self.email_verified is False:
            print(settings.EMAIL_HOST_USER)
            print(settings.EMAIL_HOST_PASSWORD)
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            subject = "Please Don't Reply"
            html_messages = render_to_string(
                template_name="emails/email_verification.html", context={'secret': secret})
            plaintext = strip_tags(html_messages)
            send_mail(
                subject, plaintext,
                settings.EMAIL_HOST_USER,
                [self.email,],
                fail_silently=False,
                html_message=html_messages
            )
            self.save()
        else:
            return

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})


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
