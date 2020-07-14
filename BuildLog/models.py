import common

from django.db import models

class BuildLogCategory(common.Category):
    pass

class BuildLogEntry(common.Entry):
    category = models.ManyToManyField(BuildLogCategory, verbose_name="Category")
    pass
