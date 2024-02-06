
from agents.models import *
from agents.tests.build_test_data import Build
from django.test import TestCase


class TestModels(TestCase):
    def setUp(self):
        Build().build_data()
        self.agent = Agent.objects.get(name="summarization_agent")

    def test_agent_user_agent_proxy(self):
        user_proxy_agent = self.agent.user_proxy_agent()




