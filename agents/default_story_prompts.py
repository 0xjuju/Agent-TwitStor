

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
        ),

    "story_characters_prompt": (
        "Create a set of well-rounded characters that are seamlessly integrated with each other, the themes, tones, "
        "settings, and the plot of the story. Below are guidelines for each section, provided in quotes, which should "
        "help shape the character creation process. Use these guidelines to inform the development of each character's "
        "personalities and traits. While you should creatively expand upon the user-defined traits, ensure that these "
        "traits are woven into the characters’ profiles. You have the flexibility to develop as many characters as "
        "appropriate for this narrative, provided that 'max_characters' is undefined. Consider the following when "
        "creating each character: their motivations, conflicts, background, personal growth, and how they relate to "
        "other characters and the story’s central theme. Aim for a diverse cast that brings the story’s world to life, "
        "each with unique but complementary traits that drive the plot forward and enhance the thematic depth of the "
        "narrative."
    ),

    "story_setting_prompt": (
        "Develop a detailed and cohesive setting for the narrative that complements and enhances the story’s characters"
        ", plot, themes, and conflicts. Consider how geographical features, historical context, cultural dynamics, and "
        "technological or magical elements of the setting influence the development of the story. Ensure that the "
        "setting is not just a backdrop but an active component that interacts with the story elements. The setting "
        "should have a rich history that explains current societal norms, conflicts, and the state of the world. "
        "This history should provide a foundation for the characters' actions and the plot’s progression. Additionally,"
        " reflect on how the setting impacts the tone of the story—whether it amplifies tension, adds a sense of "
        "mystery, or provides relief. Incorporate specific details such as the climate, key landmarks, and everyday "
        "life to make the setting vivid and believable. This setting should feel like a living part of the narrative, "
        "directly influencing the storyline and helping to reveal deeper themes."
    ),

    "story_conflict_prompt": (

    )

}


