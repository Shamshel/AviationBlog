import common

from django.db import models

class FlightLogCategory(common.Category):
    pass

class FlightLogEntry(common.Entry):
    category = models.ManyToManyField(FlightLogCategory, verbose_name="Category")
    pass
