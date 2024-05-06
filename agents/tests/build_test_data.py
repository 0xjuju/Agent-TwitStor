

from agents.models import *
from book.models import *
from book.tests.build_book_data import BuildBookData


class Build:

    def build_data(self):
        BuildBookData().build_all()
        self.build_api_keys()
        self.build_llm_configs()
        self.build_agents()
        self.build_training_sources()
        self.build_prompts()
        self.build_fine_tuned_models()
        self.build_scripts()

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
    def build_fine_tuned_models():
        fine_tuned_models = [
            FineTunedModel(
                model_id="ftjob-N8R14F286lIicXeCw0aSbvh1",
                prompt=Prompt.objects.get(name="Test Fantasy Prompt")
            )
        ]

        FineTunedModel.objects.bulk_create(fine_tuned_models)

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
    def build_prompts():
        prompt_1 = Prompt.objects.create(
                story=Story.objects.first(),
                name="Test Fantasy Prompt",
                gpt_model="davinci-002",
            )

        prompt_1.training_sources.add(TrainingSource.objects.get(name="The Wood Beyond the World"))

    @staticmethod
    def build_scripts():
        scripts = [
            Script(
                name="test script 1",
                fine_tuned_model=FineTunedModel.objects.get(prompt__name="Test Fantasy Prompt")
            ),
        ]

        Script.objects.bulk_create(scripts)

    @staticmethod
    def build_training_sources():

        sources = [
            TrainingSource(
                name="The Wood Beyond the World",
                genre="fantasy",
                source="https://www.gutenberg.org/cache/epub/3055/pg3055.txt",
                start_text="CHAPTER I",
                stop_text="*** END",
                split_text_delimiter="CHAPTER",
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











