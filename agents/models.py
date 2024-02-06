
import autogen
import decouple
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

    def user_proxy_agent(self, system_message: str, human_input_mode: str, max_consecutive_auto_reply=10)\
            -> autogen.UserProxyAgent:
        """

        :param system_message: Initial message to give agent
        :param human_input_mode: How much autonomy the agent has. Alway, never, or sometimes ask for human action
        :param max_consecutive_auto_reply: max times bots will interact before interruption
        :return: User proxy agent object
        """
        input_modes = ["TERMINATE", "NEVER", "ALWAYS"]
        if human_input_mode not in input_modes:
            raise ValueError(f"{human_input_mode} not an option. Choices are: {input_modes}")

        llm_config = self.llm_config.config

        agent = autogen.UserProxyAgent(
            name=self.name,
            human_input_mode=human_input_mode,
            max_consecutive_auto_reply=max_consecutive_auto_reply,
            code_execution_config=self._code_execution_config,
            llm_config=llm_config,
            system_message=system_message
        )

        return agent


class APIKey(models.Model):
    model_name = models.CharField(max_length=255, default="")
    value = models.CharField(max_length=255, default="")


class LLMConfig(models.Model):
    name = models.CharField(max_length=255, default="")
    api_keys = models.ManyToManyField(APIKey)
    timeout = models.IntegerField(default=600)
    cache_seed = models.IntegerField(default=42)
    temperature = models.IntegerField(default=0)

    @property
    def config(self) -> dict[str, Union[int, list, str]]:
        config_list = [{"model": i.model_name, "api_key": decouple.config(i.value)} for i in self.api_keys]
        config_file = {
            "timeout": self.timeout,
            "cache_seed": self.cache_seed,
            "config_list": config_list,
            "temperature": "temperature"
        }

        return config_file



