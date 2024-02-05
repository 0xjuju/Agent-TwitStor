from django.db import models


class Agent(models.Model):
    agent_type_choices = (
        ("assistant", "assistant", ),
        ("user_proxy", "user_proxy", ),
    )
    name = models.CharField(max_length=255, default="")
    agent_type = models.CharField(max_length=255, default="assistant")

    def __str__(self):
        return self.name



