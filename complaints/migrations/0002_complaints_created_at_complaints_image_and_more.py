# Generated by Django 5.0.1 on 2024-03-12 05:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("complaints", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaints",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="complaints",
            name="image",
            field=models.FileField(
                default=None, max_length=250, null=True, upload_to="complaints/"
            ),
        ),
        migrations.AddField(
            model_name="complaints",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
