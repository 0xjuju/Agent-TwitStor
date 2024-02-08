
from agents.models import *
from agents.tests.build_test_data import Build
from django.test import TestCase


class TestModels(TestCase):
    def setUp(self):
        Build().build_data()
        self.agent = Agent.objects.get(name="summarization_agent")

    def test_agents(self):
        user_proxy_agent = self.agent.user_proxy_agent()
        assistant_agent = self.agent.assistant_agent()
        print(assistant_agent)

        user_proxy_agent.initiate_chat(assistant_agent, message="Plot a chart of NVDA and TESLA stock price change YTD.")




