# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 18:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event_date', models.DateField(blank=True, default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('street_one', models.CharField(blank=True, max_length=255)),
                ('street_two', models.CharField(blank=True, max_length=255)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(blank=True, max_length=10)),
                ('telephone_number', localflavor.us.models.PhoneNumberField(blank=True, max_length=20)),
            ],
        ),
    ]
