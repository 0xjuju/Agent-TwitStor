import json

import autogen
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

    def user_proxy_agent(self, human_input_mode):
        input_modes = ["TERMINATE", "NEVER", "ALWAYS"]
        if human_input_mode not in input_modes:
            raise ValueError(f"{human_input_mode} not an option. Choices are: {input_modes}")

        agent = autogen.UserProxyAgent(
            name=self.name,
            human_input_mode=human_input_mode,
        )


class LLMConfig(models.Model):
    name = models.CharField(max_length=255, default="")
    model = models.CharField(max_length=255, default="")
    api_key = models.CharField(max_length=255, default="")
    timeout = models.IntegerField(default=600)
    cache_seed = models.IntegerField(default=42)
    temperature = models.IntegerField(default=0)

