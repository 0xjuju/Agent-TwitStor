from agents.models import *


class Build:

    def build_data(self):
        self.build_api_keys()
        self.build_llm_configs()
        self.build_agents()
        self.build_training_sources()

    @staticmethod
    def build_agents():
        agents = [
            Agent(
                name="assistant",
                agent_type="assistant",
                llm_config=LLMConfig.objects.get(name="assistant")
            ),

            Agent(
                name="user_proxy",
                agent_type="user_proxy",
                use_code_execution=True,
            ),

            Agent(
                name="retrieval_assistant",
                agent_type="retrieval_assistant",
                system_message="You are a helpful assistant",
                llm_config=LLMConfig.objects.get(name="retrieval_assistant")
            ),

            Agent(
                name="retrieval_user_proxy",
                agent_type="retrieval_user_proxy",

            ),

            Agent(
                name="teachable",
                agent_type="teachable",
                use_code_execution=True,
                llm_config=LLMConfig.objects.get(name="retrieval_assistant"),
            )


        ]

        Agent.objects.bulk_create(agents)

    @staticmethod
    def build_api_keys():
        keys = [
            APIKey(
                model_name="gpt-4",
                _value="OPENAI_API_KEY",
            ),
        ]

        APIKey.objects.bulk_create(keys)

    @staticmethod
    def build_llm_configs():
        api_key = APIKey.objects.get(model_name="gpt-4")

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
    def build_training_sources():

        sources = [
            TrainingSource(
                name="The Wood Beyond the World",
                genre="fantasy",
                source="https://www.gutenberg.org/cache/epub/3055/pg3055.txt"
            ),

            TrainingSource(
                name="A Faerie Romance for Men and Women",
                genre="fantasy",
                source="https://www.gutenberg.org/cache/epub/325/pg325.txt"
            ),

            TrainingSource(
                name="The King of Elfland's Daughter",
                genre="fantasy",
                source="https://www.gutenberg.org/cache/epub/61077/pg61077.txt"
            ),
        ]

        TrainingSource.objects.bulk_create(sources)











