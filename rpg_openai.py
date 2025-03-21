import openai
import os

openai.api_key = "[Insert OpenAI API Key Here]"

def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = """ 
    You are an AI that generates a text-based RPG story with branching decisions. Please write a metafiction horror story that follows an unnamed protagonist as they wake up in a dark place and attempt to escape.
    
    The story should follow this specific format (ensure there are no blank lines between each line of text):

    [Event ID] | [Event Description] | [Choice 1 Description] | [Choice 2 Description] | [Next Event ID for Choice 1] | [Next Event ID for Choice 2]

    For example:
    1 | You awaken in a bizarre alien landscape. Do you: 1) Search for your crashed starship 2) Look for signs of intelligent life | 2 | 3
    2 | You find your starship crashed into a crystalline formation. Do you: 1) Check the ship for supplies 2) Try to repair the communications system | 4 | 5
    3 | You see structures in the distance suggestive of intelligent life. Do you: 1) Head towards the structures 2) Try to avoid potential danger by taking a different path | 7 | 8
    ...

    Please generate a similar branching RPG story with 10 unique decision points and a minimum tree depth of 6. The structure should be consistent, and each event should have a description followed by two choices, leading to different outcomes based on the choices.
    The Next Event ID for all endings should be "-1". Let all possible outcomes be connected in the following way: the protagonist grows aware of the fact that they are in a text-based RPG, a story, and senses the presence of the player before they appear to die upon finishing the story. 
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def save_story_to_file(filename, story_text):
    with open(filename, "w") as story_file:
        story_file.write(story_text)

if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("story.txt", story_text)
