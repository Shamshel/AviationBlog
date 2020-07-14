import common

from django.db import models

class BuildBlogCategory(common.Category):
    pass

class BuildBlogEntry(common.Entry):
    category = models.ManyToManyField(BuildBlogCategory, verbose_name="Category")
    pass
