#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Jeremy Low

from django.forms import ModelForm

from signin_sheets.models import EventParticipant


class ParticipantSigninForm(ModelForm):
    """Form to sign in an event participant."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'autocomplete': 'off'
            })

    class Meta:
        """Class specific attrs. Required for ModelForm."""

        model = EventParticipant
        fields = [
            'first_name',
            'last_name',
            'email',
            'street_one',
            'street_two',
            'state',
            'zip_code',
            'telephone_number',
        ]
