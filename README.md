## Description
Use AI Agents to create short stories. Training data of
selected books are used to finetune the model. Bayesian Optimization is used to adjust the parameters of the fine-tuned
model for optimal fitting of training data. When there are multiple viable training sources, a different agent analyzes
the different datasets and analyzes the user input for the to-be-created story details. This agent will rank these 
datasets and determine which of them should be used to finetune the model. Once the model is fine-tuned, a "Writer" agent
will create the story, and then "Audience" and "Critic" agents are used to critique the work.

### <u>Writer Agent<u/>
Uses retrieval augmentation to learn the structure and styles of highly acclaimed novels and writing styles. Given user
context about characters, settings, tone, conflicts etc., this agent will create a short story combining these ideas with
a well-structured writing format and story transition.

### <u>Audience Agenet<u/>
Learn different aspects of what users tend to like about books (characters, plot, story transition etc.) through public,
and use this knowledge to score the Writer agent's work on a scale of 1-10, giving insight into which parts of the story
should be refactored to gain a higher score

### <u>Critic Agent<u/>
Learn how professional critics score different aspects of novels, and then repeat the same process as the Audience agent 
 for giving input on how the Writer agent's content should be refactored


The process goes as follows:
- Writer agent creates content based on user inputs about character, plot etc.
- Audience and Critic agents rate the material based on the "Scoring Criteria"
- Both agents recommend improvements that would improve the Writer's score
- The Writer agent considers both the score and recommendations, and refactors relevant parts of the story
- The content is then scored again by the agents, and again the Writer takes the feedback and refactors certain parts

This process is repeated until the average Audience/Critic score exceeds a value between 1 and 10, as input by the user.
Additionally, a weight can be added to make the average score more or less partial between the Audience and Critic bot
