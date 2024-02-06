
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

    def assistant_agent(self, is_termination_message=None, max_consecutive_auto_reply=10,
                        human_input_mode="Never", description=None) -> autogen.AssistantAgent:
        """

        :param is_termination_message:
        :param max_consecutive_auto_reply:
        :param human_input_mode:
        :param description:
        :return:
        """
        agent = autogen.AssistantAgent(
            name=self.name,
            system_message=self.system_message,
            llm_config=self.llm_config.value,
            is_termination_msg=is_termination_message,
            human_input_mode=human_input_mode,
            max_consecutive_auto_reply=max_consecutive_auto_reply,
            description=description
        )

        return agent

    def code_execution_config(self, **kwargs) -> Union[dict[str, str], bool]:

        if self._code_execution_config:
            return {
                "work_dir": kwargs["work_dir"],
                "use_docker": "python:3",
            }
        else:
            return False

    def user_proxy_agent(self,
                         human_input_mode: str = "ALWAYS",
                         max_consecutive_auto_reply=10,
                         is_termination_message=None,
                         function_map=None,
                         default_auto_reply="",
                         description=""
                         ) -> autogen.UserProxyAgent:
        """

        :param human_input_mode: How much autonomy the agent has. Always, never, or sometimes ask for human action
        :param max_consecutive_auto_reply: max times bots will interact before interruption
        :param is_termination_message: ...
        :param function_map: Callable function for agent to use
        :param default_auto_reply: Default message when no code execution or LLM is generated
        :param description: Short description of agent, Used by other agents to decide when to call this agent
        :return: User proxy agent object
        """
        input_modes = ["TERMINATE", "NEVER", "ALWAYS"]
        if human_input_mode not in input_modes:
            raise ValueError(f"{human_input_mode} not an option. Choices are: {input_modes}")

        llm_config = self.llm_config.value

        agent = autogen.UserProxyAgent(
            name=self.name,
            human_input_mode=human_input_mode,
            max_consecutive_auto_reply=max_consecutive_auto_reply,
            code_execution_config=self._code_execution_config,
            llm_config=llm_config,
            system_message=self.system_message,
            is_termination_msg=is_termination_message,
            function_map=function_map,
            default_auto_reply=default_auto_reply,
            description=description

        )

        return agent


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
            "temperature": "temperature"
        }

        return config_file



