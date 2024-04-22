
from django.db import models


class BaseStory(models.Model):
    story = models.ForeignKey("Story", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Character(BaseStory):
    name = models.CharField(max_length=155, default="", blank=True)
    birthday = models.DateField()
    background = models.TextField(default="", blank=True)


class Setting(BaseStory):
    description = models.TextField(default="", blank=True)
    timeline = models.DateField(null=True)


class Story(models.Model):
    message = models.CharField(max_length=255, default="")


class Tone(BaseStory):
    name = models.CharField(max_length=255, default="")





