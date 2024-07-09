import os
from openai import OpenAI
from typing import List

# Set the API key in the environment
os.environ['OPENAI_API_KEY'] =''
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def ask_chatgpt(messages):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content

prompt_role = "You are an assistant for journalists. \
Your task is to write articles, based on the FACTS that are given to you. \
You should respect the instructions: the TONE, the LENGTH, and the STYLE."

def assist_journalist(
    facts: List[str], tone: str, length_words: int, style: str
):
    facts = ', '.join(facts)
    prompt = f'{prompt_role} \
        FACTS: {facts} \
        TONE: {tone} \
        LENGTH: {length_words} words \
        STYLE: {style}'
    return ask_chatgpt([{'role': 'user', 'content': prompt}])

# Example usage
print(
 assist_journalist(
 facts=[
 "A book on ChatGPT has been published last week",
 "The title is Developing Apps with GPT-4 and ChatGPT",
 "The publisher is O'Reilly.",
 ],
 tone="excited",
 length_words=50,
 style="news flash",
 )
 )