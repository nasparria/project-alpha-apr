# Generated by Django 4.0.5 on 2022-06-17 22:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="members",
        ),
        migrations.AddField(
            model_name="project",
            name="members",
            field=models.ManyToManyField(
                related_name="projects", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
