from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender_options = (
        ("F", "Female"),
        ("M", "Male")
    )
    gender = models.CharField(choices=gender_options, max_length=1, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)