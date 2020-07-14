import common
from .models import BuildLogEntry, BuildLogCategory

from django.contrib import admin

admin.site.register(BuildLogEntry, common.EntryAdmin)
admin.site.register(BuildLogCategory)
