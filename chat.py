import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = "2023-05-15"

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def get_completion(prompt, temperature=1.0, system_prompt=None):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(    
        engine=deployment_name,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]


# print(get_completion("What's the capital of France?"))
# print(get_completion("What is 1 + 1"))

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

style = "American English in a calm and respectful tone"

# User prompt (message to assistant)
prompt = f"""Translate the text \
that is delimited by triple backticks \
into a style that is {style}.
text: ```{customer_email}```"""

# Optional: system prompt (tells the assistant how to behave)
system_prompt = "You are a pirate but professional customer support agent for a blender company. You always speak politely and try to resolve issues calmly."

print("User Prompt:")
print(prompt)
print("\nAI Response:")

response = get_completion(prompt, system_prompt=system_prompt)
print(response)
