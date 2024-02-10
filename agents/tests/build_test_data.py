import autogen
from agents.models import *


class Build:

    def build_data(self):
        self.build_api_keys()
        self.build_llm_configs()
        self.build_user_proxy_agents()
        self.build_assistant_agent()
        self.build_retrieval_assistants()
        self.build_retrieval_user_proxy()

    @staticmethod
    def build_api_keys():
        keys = [
            APIKey(
                model_name="gpt-3.5-turbo",
                _value="OPENAI_API_KEY",
            ),
        ]

        APIKey.objects.bulk_create(keys)

    @staticmethod
    def build_llm_configs():
        api_key = APIKey.objects.get(model_name="gpt-3.5-turbo")

        config1 = LLMConfig.objects.create(
            name="assistant",
            timeout=600,
            cache_seed=42,
            temperature=0,
        )
        config1.save()
        config1.api_keys.add(api_key)

        config2 = LLMConfig.objects.create(
            name="user_proxy",
            timeout=600,
            cache_seed=42,
            temperature=0,
        )
        config2.save()
        config2.api_keys.add(api_key)

        config3 = LLMConfig.objects.create(
            name="retrieval_assistant",
            timeout=600,
            cache_seed=42,
            temperature=0,
        )
        config3.save()
        config3.api_keys.add(api_key)

    @staticmethod
    def build_assistant_agent():
        config = LLMConfig.objects.get(name="assistant")
        agents = [
            Agent(
                name="assistant",
                agent_type="assistant",
                llm_config=config
            )
        ]

        Agent.objects.bulk_create(agents)

    @staticmethod
    def build_user_proxy_agents() -> None:
        config = LLMConfig.objects.get(name="user_proxy")

        agents = [
            Agent(
                name="user_proxy",
                agent_type="user_proxy",
                use_code_execution=True,
            )
        ]

        Agent.objects.bulk_create(agents)

    @staticmethod
    def build_retrieval_assistants():
        agents = [
            Agent(
                name="retrieval_assistant",
                agent_type="retrieval_assistant",
                system_message="You are a helpful assistant",
                llm_config=LLMConfig.objects.get(name="retrieval_assistant")
            )
        ]

        Agent.objects.bulk_create(agents)

    @staticmethod
    def build_retrieval_user_proxy():
        agents = [
            Agent(
                name="retrieval_user_proxy",
                agent_type="retrieval_user_proxy",

            )
        ]

        Agent.objects.bulk_create(agents)



