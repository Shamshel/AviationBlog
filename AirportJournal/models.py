import common

from django.db import models

class AirportJournalCategory(common.Category):
    pass

class AirportJournalEntry(common.Entry):
    category = models.ManyToManyField(AirportJournalCategory, verbose_name="Category")
    pass
