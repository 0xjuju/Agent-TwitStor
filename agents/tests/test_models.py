
from agents.models import *
from agents.tests.build_test_data import Build
from django.test import TestCase


class TestModels(TestCase):
    def setUp(self):
        Build().build_data()
        self.user_agent = Agent.objects.get(name="user_proxy")
        self.assistant = Agent.objects.get(name="assistant")

    def test_agents(self):
        user_proxy_agent = self.user_agent.get_agent()
        assistant_agent = self.assistant.get_agent()

        user_proxy_agent.initiate_chat(assistant_agent, message="Plot a chart of NVDA and TESLA stock price change YTD.")






