
from autogen import AssistantAgent, ConversableAgent, UserProxyAgent
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.contrib.capabilities.teachability import Teachability
import decouple
from django.db import models
from typing import Union


class Agent(models.Model):
    agent_type_choices = (
        ("assistant", "assistant", ),
        ("user_proxy", "user_proxy", ),
        ("retrieval_assistant", "retrieval_assistant",),
        ("retrieval_user_proxy", "retrieval_user_proxy",),
    )

    human_input_choices = (
        ("NEVER", "NEVER",),
        ("ALWAYS", "ALWAYS",),
        ("TERMINATE", "TERMINATE", ),
    )

    name = models.CharField(max_length=255, default="")
    agent_type = models.CharField(max_length=255, default="assistant")
    use_code_execution = models.BooleanField(default=False)
    system_message = models.CharField(max_length=255, default="")
    human_input_mode = models.CharField(max_length=255, default="ALWAYS", choices=human_input_choices)
    max_consecutive_reply = models.IntegerField(default=10)
    _is_termination_message = models.BooleanField(default=False)
    description = models.TextField(default="")
    use_docker = models.BooleanField(default=False)
    llm_config = models.ForeignKey("LLMConfig", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_agent(self, **kwargs) -> Union[
        UserProxyAgent,
        AssistantAgent,
        RetrieveAssistantAgent,
        RetrieveUserProxyAgent,
        None
    ]:
        fields = {
            "name": self.name,
            "max_consecutive_auto_reply": self.max_consecutive_reply,
            "code_execution_config": self.code_execution_config() if self.use_code_execution else {}
        }

        if self.human_input_mode:
            fields["human_input_mode"] = self.human_input_mode

        if self.system_message:
            fields["system_message"] = self.system_message

        if self.llm_config:
            fields["llm_config"] = self.llm_config.value

        if self._is_termination_message:
            fields["is_termination_msg"] = lambda x: x.get("content", "").rstrip().endswith("TERMINATE")

        if self.agent_type == "user_proxy":
            agent = UserProxyAgent(**fields)

        elif self.agent_type == "assistant":
            agent = AssistantAgent(**fields)

        elif self.agent_type == "retrieval_user_proxy":
            fields["retrieve_config"] = {
                "task": kwargs["task"],
                "docs_path": kwargs["docs_path"],
            }
            agent = RetrieveUserProxyAgent(**fields)

        elif self.agent_type == "retrieval_assistant":
            agent = RetrieveAssistantAgent(**fields)

        elif self.agent_type == "teachable":
            agent = ConversableAgent(**fields)
            teachability = Teachability(
                reset_db=kwargs.get("reset_db"),
                path_to_db_dir="./tmp/teachability_db"
            )

            teachability.add_to_agent(agent)

        else:
            raise ValueError(f"No agent type selected. '{self.agent_type}' not a valid choice")

        return agent

    def code_execution_config(self) -> Union[dict[str, str], dict]:

        if self.use_code_execution:
            return {
                "work_dir": "coding",
                "use_docker": False,
            }
        else:
            return {}


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


class Prompt(models.Model):
    story = models.ForeignKey("book.Story", on_delete=models.SET_NULL, null=True)
    training_sources = models.ManyToManyField("TrainingSource")
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="", blank=True)
    initial_prompt = models.TextField(default="", blank=True)


class TrainingSource(models.Model):
    name = models.CharField(max_length=255, default="")
    genre = models.CharField(max_length=255, default="")
    source = models.CharField(max_length=255, default="")



