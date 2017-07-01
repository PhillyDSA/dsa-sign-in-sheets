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
    event_date = models.DateField(default=datetime.date.today, required=False)


class EventParticipant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(required=False)
    street_one = models.CharField(max_length=255, required=False)
    street_two = models.CharField(max_length=255, required=False)
    state = USStateField(required=False)
    zip_code = USZipCodeField(required=False)
    telephone_number = PhoneNumberField(required=False)
