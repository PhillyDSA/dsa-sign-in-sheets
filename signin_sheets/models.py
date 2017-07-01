import datetime

from django.db import models
from localflavor.us.models import (
    PhoneNumberField,
    USZipCodeField,
    USStateField,
)

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    event_date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return f'{self.name} ({self.event_date})'


class EventParticipant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    street_one = models.CharField(max_length=255, blank=True)
    street_two = models.CharField(max_length=255, blank=True)
    state = USStateField(blank=True)
    zip_code = USZipCodeField(blank=True)
    telephone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name or ""} ({self.email or "[No Email Given]"})'
