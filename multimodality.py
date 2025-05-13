# from langchain_openai import AzureChatOpenAI
# from langchain_core.messages import HumanMessage
# from dotenv import load_dotenv
# import os

# # Load .env where OPENAI_API_KEY is stored
# load_dotenv()

# # Initialize GPT-4o (or gpt-4-vision-preview)
# chat = AzureChatOpenAI(
#     temperature=0.0,
#     deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
#     api_key=os.getenv("AZURE_OPENAI_KEY"),
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     api_version="2024-08-01-preview"
# )

# # Construct multimodal message with image and text
# message = HumanMessage(content=[
#     {"type": "text", "text": "What do you see in this image?"},
#     {
#         "type": "image_url",
#         "image_url": {
#             "url": "https://upload.wikimedia.org/wikipedia/commons/9/99/Black_square.jpg"
#         }
#     }
# ])
# response = chat.invoke([message])
# print(" Model Response:\n", response.content)

import base64
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

chat = AzureChatOpenAI(
    temperature=0.0,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2023-05-15"
)

with open("weather 1.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe the weather in this image:"},
        {
            "type": "image",
            "source_type": "base64",
            "data": base64_image,
            "mime_type": "image/jpeg",
        }
    ]
)

response = chat.invoke([message])
print("Model Response:\n", response.content)