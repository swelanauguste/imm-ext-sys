import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    pass


class Profile(models.Model):
    GENDER_LIST = [
        ("F", "Female"),
        ("M", "Male"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    officer_id = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    phone = models.CharField(max_length=25, null=True, default="+1")
    phone1 = models.CharField(max_length=25, blank=True)

    def get_absolute_url(self):
        return reverse("profile-detail", kwargs={"pk": self.pk})

    def __str__(self):
        if self.last_name and self.officer_id:
            return f"{self.last_name} {self.officer_id}"
        return self.user.email
