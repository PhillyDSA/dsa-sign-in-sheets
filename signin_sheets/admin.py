from django.contrib import admin

from signin_sheets.models import Event, EventParticipant


admin.site.register(Event)
admin.site.register(EventParticipant)
