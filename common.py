from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

STATUS = (
        (0, "Draft"),
        (1, "Publish")
        )

# Log entry base classes
class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")

    class Meta:
        abstract = True
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]

    def __str__(self):
        return self.title

class Entry(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, default="new_post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related')
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Updated")
    content = models.TextField(verbose_name="Body")
    created_on = models.DateTimeField(auto_now=True, verbose_name="Created")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        abstract = True
        ordering = ["-created_on"]
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ["-created_on", "title"]

    def __str__(self):
        return self.title

# Log entry admin base classes
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
