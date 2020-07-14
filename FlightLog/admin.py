import common
from .models import FlightLogEntry, FlightLogCategory

from django.contrib import admin

admin.site.register(FlightLogEntry, common.EntryAdmin)
admin.site.register(FlightLogCategory)
