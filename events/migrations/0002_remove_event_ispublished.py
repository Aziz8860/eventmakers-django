# Generated by Django 5.2 on 2025-04-17 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="isPublished",
        ),
    ]
