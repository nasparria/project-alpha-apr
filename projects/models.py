from django.db import models
from django.conf import settings

UserModel = settings.AUTH_USER_MODEL
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(UserModel, related_name="projects")

    def __str__(self):
        return self.name
