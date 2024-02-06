from django.db import models
from typing import Union


class Agent(models.Model):
    agent_type_choices = (
        ("assistant", "assistant", ),
        ("user_proxy", "user_proxy", ),
    )
    name = models.CharField(max_length=255, default="")
    agent_type = models.CharField(max_length=255, default="assistant")
    _code_execution_config = models.BooleanField(default=True)
    system_message = models.CharField(max_length=255, default="")
    llm_config = models.ForeignKey("LLMConfig", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def code_execution_config(self, **kwargs) -> Union[dict[str, str], bool]:

        if self._code_execution_config:
            return {
                "work_dir": kwargs["work_dir"],
                "use_docker": "python:3",
            }
        else:
            return False


class LLMConfig(models.Model):
    name = models.CharField(max_length=255, default="")
    config_list = models.TextField(default="")
    timeout = models.IntegerField(default=600)
    cache_seed = models.IntegerField(default=42)
    temperature = models.IntegerField(default=0)



