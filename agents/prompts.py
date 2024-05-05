from agents.default_story_prompts import default_prompts

"""

@use_default_prompt decorator is used to check if prompt=None. If it does, default_prompts are used.
"""


def use_default_prompt(func):
    def wrapper(**kwargs):
        prompt = kwargs.get("prompt")
        if prompt is None:

            return func(prompt=default_prompts[func.__name__])
        else:
            return func(**kwargs)
    return wrapper


@use_default_prompt
def story_training_prompt(prompt=None):
    return prompt


@use_default_prompt
def story_training_completion(prompt=None):
    return prompt

