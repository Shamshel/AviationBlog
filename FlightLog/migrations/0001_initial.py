# Generated by Django 3.0.7 on 2020-07-14 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightLogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlightLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(default='new_post', max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('content', models.TextField(verbose_name='Body')),
                ('created_on', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flightlog_flightlogentry_related', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='FlightLog.FlightLogCategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
                'ordering': ['-created_on', 'title'],
                'abstract': False,
            },
        ),
    ]
