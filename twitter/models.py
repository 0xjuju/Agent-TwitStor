from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255, default="")
    username = models.CharField(unique=True, max_length=255, default="")
    user_id = models.BigIntegerField(default=0)
    website = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    medium = models.URLField(max_length=255)


