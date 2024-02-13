from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255, default="")
    username = models.CharField(unique=True, max_length=255, default="")
    user_id = models.BigIntegerField(default=0)
    website = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    medium = models.URLField(max_length=255)
    follower_count = models.IntegerField(default=0)


class Post(models.Model):
    post_id = models.BigIntegerField(default=0)
    post_date = models.DateTimeField(null=True)
    description = models.TextField(default="")
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    account = models.ForeignKey(Account, models.CASCADE)
    image = models.ImageField(null=True)


