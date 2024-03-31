# Generated by Django 5.0.1 on 2024-03-06 12:41

import autoslug.fields
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "news_image",
                    models.FileField(
                        default=None, max_length=250, null=True, upload_to="cards/"
                    ),
                ),
                ("news_title", models.CharField(max_length=100)),
                ("news_content", tinymce.models.HTMLField()),
                (
                    "news_slug",
                    autoslug.fields.AutoSlugField(
                        default=None,
                        editable=False,
                        null=True,
                        populate_from="news_title",
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
