import common
from .models import AirportJournalEntry, AirportJournalCategory

from django.contrib import admin

admin.site.register(AirportJournalEntry, common.EntryAdmin)
admin.site.register(AirportJournalCategory)
