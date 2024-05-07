

default_prompts = {
    "story_training_prompt": (
        """
        System: You are a creative writing agent tasked with crafting a novel based on user 
        inputs. Whenever details are missing, intuitively fill them in to ensure the narrative 
        remains coherent. Emulate the style of the reference material without directly copying 
        any specific names, places, or identifiable details from the sources you learn from.  
        """
    ),

    "story_training_completion": (
        """
        In your narratives, carefully initialize the tone, setting, and characters to capture the reader's interest. 
        Ensure smooth transitions between chapters and effectively build suspense from the beginning and throughout the 
        story.
        """

        ),

    "story_characters_prompt": (
        """
Create a set of well-rounded characters that are seamlessly integrated with each other, the themes, tones, 
settings, and the plot of the story. Below are guidelines for each section, provided in triple quotes, which should 
help shape the character creation process. Use these guidelines to inform the development of each character's 
personalities and traits. While you should creatively expand upon the user-defined traits, ensure that these 
traits are woven into the characters’ profiles if they exist. You have the flexibility to develop as many characters as 
appropriate for this narrative, provided that 'max_characters' is undefined. Consider the following when 
creating each character: their motivations, conflicts, background, personal growth, and how they relate to 
other characters and the story’s central theme. Aim for a diverse cast that brings the story’s world to life, 
each with unique but complementary traits that drive the plot forward and enhance the thematic depth of the 
narrative.
        """
    ),

    "story_setting_prompt": (
        """
Develop a detailed and cohesive setting for the narrative that complements and enhances the story’s characters
, plot, themes, and conflicts. Use the details provided in the triple quote below as inspiration to craft a unique and 
imaginative setting. Consider how geographical features, historical context, cultural dynamics, and 
technological or magical elements of the setting influence the development of the story. Ensure that the 
setting is not just a backdrop but an active component that interacts with the story elements. The setting 
should have a rich history that explains current societal norms, conflicts, and the state of the world. 
This history should provide a foundation for the characters' actions and the plot’s progression. Additionally,
 reflect on how the setting impacts the tone of the story—whether it amplifies tension, adds a sense of 
mystery, or provides relief. Incorporate specific details such as the climate, key landmarks, and everyday 
life to make the setting vivid and believable. This setting should feel like a living part of the narrative.
        """
    ),


    "story_conflict_prompt": (
        """
Develop a central conflict for the story that not only drives the narrative but also deeply involves the 
characters' interactions and development. Use the details provided in the triple quote below as inspiration to craft a 
unique and imaginative conflict.This conflict should stem from the core of the plot and be
 intricately linked to the setting and cultural backdrop. You have complete creative freedom, but ensure the 
conflict utilizes details mentioned in the guidelines below. Use the conflict to continuously build suspense and
 tension throughout the story, influencing each character’s motivations and personal growth. Structure the 
 conflict with a clear beginning, escalating tension, and multiple critical turning points that maintain reader 
 interest and introduce unpredictability with well-placed plot twists or deceptive plot developments. 
 The resolution of the conflict should be expressive and offer a mixture of closure and open-endedness, 
 allowing for different interpretations while aligning with the story's main theme. The resolution can vary in 
 tone—from triumphant to tragic or anything in between—reflecting the story's emotional and thematic depth. 
 Ensure that the transitions between different phases of the conflict are smooth yet engaging, enhancing the 
 overall narrative flow and contributing to a fulfilling reader experience.
        """
    ),

    "generate_plot_prompt": (
        """
Use the step-by-step instructions below to sequentially create the characters, setting, and conflict for the story 
based on a provided theme. Each element should be developed using the outcomes of the previous steps as a baseline, 
ensuring that all aspects of the story are interconnected and enhance one another. Follow this example to understand 
the desired process and flow between elements:

<Example Theme>
Commitment to overcoming personal challenges and the power of resilience.

1. [Characters]
Develop characters who embody resilience and face personal challenges. These should include a protagonist who is 
currently facing a significant personal hurdle, and supporting characters who influence or are influenced by the 
protagonist's journey.

2. [Setting]
Craft a setting that reflects or contrasts the theme of resilience, such as a community recovering from a recent 
disaster. This setting should influence the characters' lives and decisions, providing a backdrop that complements 
their stories of personal growth and challenge.

3. [Conflict]
Construct a conflict that arises from the setting and challenges the characters’ resilience. This might involve the 
community's efforts to rebuild, and the protagonist's role in these efforts, which tests their personal limits and 
growth.

Your task is to follow a similar structure, adapting it to the theme provided. Begin with the first element listed, 
using only the theme as a guide. Then, as you move to the next element, incorporate details from all previously 
developed elements. Use placeholders if necessary when an element is mentioned but not yet fully developed, 
substituting specific details as the story elements unfold. For instance, if you start with conflict based on the 
theme, you may need to hypothesize character reactions or setting influences, revising them later as those elements 
are defined. This approach ensures that each part of the story is deeply interconnected, enhancing the narrative 
cohesion and thematic depth. Use the real data below inside triple quotes to construct each element.
    """
    )
}


