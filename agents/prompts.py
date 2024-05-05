

"""

@use_default_prompt decorator is used to check if prompt=None. If it does, default_prompts are used.
"""

default_prompts = {
    "story_training_prompt": (
        "System: You are a creative writing agent tasked with crafting a novel based on user "
        "inputs. Whenever details are missing, intuitively fill them in to ensure the narrative "
        "remains coherent. Emulate the style of the reference material without directly copying "
        "any specific names, places, or identifiable details from the sources you learn from."
    ),

    "story_training_completion": (
            "In your narratives, carefully initialize the tone, "
            "setting, and characters to capture the reader's "
            "interest. Ensure smooth transitions between chapters"
            " and effectively build suspense from the beginning "
            "and throughout the story."
        )
}


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

