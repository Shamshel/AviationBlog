import common
from .models import BuildBlogEntry, BuildBlogCategory

from django.contrib import admin

admin.site.register(BuildBlogEntry, common.EntryAdmin)
admin.site.register(BuildBlogCategory)
