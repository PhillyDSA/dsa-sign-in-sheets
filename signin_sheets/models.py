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


class EventParticipant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    street_one = models.CharField(max_length=255, blank=True)
    street_two = models.CharField(max_length=255, blank=True)
    state = USStateField(blank=True)
    zip_code = USZipCodeField(blank=True)
    telephone_number = PhoneNumberField(blank=True)
