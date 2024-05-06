
from agents.models import *
from agents.tests.build_test_data import Build
from django.test import TestCase


class TestModels(TestCase):
    def setUp(self):
        Build().build_data()
        self.user_agent = Agent.objects.get(name="user_proxy")
        self.assistant = Agent.objects.get(name="assistant")
        self.rag_user_proxy = Agent.objects.get(name="retrieval_user_proxy")
        self.rag_assistant = Agent.objects.get(name="retrieval_assistant")
        self.teacher = Agent.objects.get(name="teachable")

    def test_agents(self):
        user_proxy_agent = self.user_agent.get_agent()
        assistant_agent = self.assistant.get_agent()

        user_proxy_agent.initiate_chat(assistant_agent, message="Plot a chart of NVDA and TESLA stock price change YTD.")

    def test_break_text_gt_max_tokens(self):
        text = ["one", "two", "three 3 3 !", "four", "five"]
        new_text = Prompt.objects.get(name="Test Fantasy Prompt").break_text_gt_max_tokens(text)
        print(new_text)

    def test_clean_training_data(self):
        training_data = TrainingSource.get_data_from_url("https://www.gutenberg.org/cache/epub/3055/pg3055.txt")

    def test_create_fine_tuned_model(self):
        f = FineTunedModel.objects.first()
        f.upload_training_data_to_openai()
        f.create_finetune_model()

    def test_get_data_from_url(self):
        data = TrainingSource.get_data_from_url("https://www.gutenberg.org/cache/epub/3055/pg3055.txt")
        self.assertEqual(data.status_code, 200)

    def test_get_ft_model(self):
        ft_model = FineTunedModel.objects.get(prompt__name="Test Fantasy Prompt").get_ft_model()
        self.assertEqual(ft_model.id, "ftjob-N8R14F286lIicXeCw0aSbvh1")

    def test_rag_agents(self):
        rag_proxy_agent = self.rag_user_proxy.get_agent(
            task="qa",
            docs_path="https://raw.githubusercontent.com/microsoft/autogen/main/README.md"
        )
        rag_assistant = self.rag_assistant.get_agent()

        rag_proxy_agent.initiate_chat(rag_assistant, problem="What is Autogen")

    def test_save_completion_pairs(self):
        prompt = Prompt.objects.get(name="Test Fantasy Prompt")
        prompt.save_completion_pairs()

    def test_teachable_agent(self):
        user = self.user_agent.get_agent()
        teacher_agent = self.teacher.get_agent(reset_db=True)

        teacher_agent.initiate_chat(user,
                                    message="Greetings, I'm a teachable user assistant! What's on your mind today?")

    def test_upload_training_data_to_openai(self):
        m = FineTunedModel.objects.first()
        m.upload_training_data_to_openai()

        updated = FineTunedModel.objects.filter(model_id=m.model_id).exists()
        self.assertTrue(updated)















