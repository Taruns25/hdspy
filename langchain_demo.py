'''
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
temperature=0.7

chat = AzureChatOpenAI(
    temperature=temperature,
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-05-15",
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT")
)


deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

chat = AzureChatOpenAI(temperature)
chat
'''

from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv(find_dotenv())

# Define model deployment name and temperature
llm_model = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # Deployment name
temperature = 0.7  # For output

# Instantiate ChatOpenAI with Azure config
chat = AzureChatOpenAI(
    temperature=temperature,
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-05-15",
    deployment_name=llm_model
)

template_string = """
Please rewrite the text that is delimited by triple backticks, into a style that is  {style}.
Text: ```{text}```
"""
prompt_template = ChatPromptTemplate.from_template(template_string)

text = """Arrr, I be fuming that me blender lid flew off and splattered me kitchen walls with smoothie! 
And to make matters worse, the warranty don't cover the cost of cleaning up me kitchen. 
I need yer help right now, matey!"""

style = "Jamaican English but a calm and respectful tone"

messages = prompt_template.format_messages(style=style, text=text)

response =chat.invoke(messages)

print(response.content)

service_reply = """Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!
"""

service_style_pirate = """\
a polite tone \
that speaks in Jamaican English \
"""

service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply)

response1 = chat.invoke(service_messages)
print(response1.content)