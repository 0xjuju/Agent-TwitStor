
import autogen
import decouple
from django.db import models
from typing import Union


class Agent(models.Model):
    agent_type_choices = (
        ("assistant", "assistant", ),
        ("user_proxy", "user_proxy", ),
    )

    human_input_choices = (
        ("NEVER", "NEVER",),
        ("ALWAYS", "ALWAYS",),
        ("TERMINATE", "TERMINATE",),
    )

    name = models.CharField(max_length=255, default="")
    agent_type = models.CharField(max_length=255, default="assistant")
    _code_execution_config = models.BooleanField(default=True)
    system_message = models.CharField(max_length=255, default="")
    human_input_mode = models.CharField(max_length=255, default="ALWAYS", choices=human_input_choices)
    max_consecutive_reply = models.IntegerField(default=0)
    _is_termination_message = models.BooleanField(default=False)
    description = models.TextField(default="")
    llm_config = models.ForeignKey("LLMConfig", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_agent(self) -> Union[
        autogen.UserProxyAgent,
        autogen.AssistantAgent
    ]:

        llm_config = self.llm_config.value if self.llm_config else None

        fields = {
            "name": self.name,
            "llm_config": llm_config,
            "is_termination_message": None,
            "human_input_mode": self.human_input_mode,
            "max_consecutive_auto_reply": self.max_consecutive_reply
        }

        if self.agent_type == "user_proxy":
            return autogen.UserProxyAgent(**fields)

        elif self.agent_type == "assistant":
            return autogen.AssistantAgent(**fields)

    def code_execution_config(self, **kwargs) -> Union[dict[str, str], bool]:

        if self._code_execution_config:
            return {
                "work_dir": kwargs["work_dir"],
                "use_docker": "python:3",
            }
        else:
            return False


class APIKey(models.Model):
    model_name = models.CharField(max_length=255, default="")
    _value = models.CharField(max_length=255, default="")

    def get_key(self):
        return decouple.config(self._value)


class LLMConfig(models.Model):
    name = models.CharField(max_length=255, default="")
    api_keys = models.ManyToManyField(APIKey)
    timeout = models.IntegerField(default=600)
    cache_seed = models.IntegerField(default=42)
    temperature = models.IntegerField(default=0)

    @property
    def value(self) -> dict[str, Union[int, list, str]]:
        config_list = [{"model": i.model_name, "api_key": i.get_key()} for i in self.api_keys.all()]
        config_file = {
            "timeout": self.timeout,
            "cache_seed": self.cache_seed,
            "config_list": config_list,
            "temperature": self.temperature
        }

        return config_file



