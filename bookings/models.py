from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validators import phone_validator


class Book(models.Model):
    resident = models.ForeignKey("Resident", on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name="bookings")
    start = models.DateTimeField(_("Start date"))
    end = models.DateTimeField(_("End date"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.resident} - {self.room}"


class Resident(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, validators=[phone_validator], null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
