from agents.prompts import use_default_prompt, default_prompts
from django.test import TestCase


class TestDecorators(TestCase):
    def setUp(self):
        pass

    def test_use_default_prompt(self):

        @use_default_prompt
        def story_training_prompt(prompt=None):
            return prompt

        is_default = story_training_prompt()
        not_default = story_training_prompt(prompt="Not a default prompt")

        self.assertEqual(is_default, default_prompts["story_training_prompt"])
        self.assertEqual(not_default, "Not a default prompt")


