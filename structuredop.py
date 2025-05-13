from pydantic import BaseModel, Field
from langchain_openai import AzureChatOpenAI  # ✅ NEW import
import os
from dotenv import load_dotenv, find_dotenv

# Load .env with Azure details
load_dotenv(find_dotenv())

# Define Pydantic schema
class ResponseFormatter(BaseModel):
    answer: str = Field(description="The answer to the user's question")
    followup_question: str = Field(description="A follow-up question for the user")

# Use the updated AzureChatOpenAI
chat = AzureChatOpenAI(
    temperature=0.0,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-08-01-preview"
)

# Bind the schema
model_with_tools = chat.bind_tools([ResponseFormatter])

ai_msg = model_with_tools.invoke("What is the powerhouse of the cell?")

tool_call_args = ai_msg.tool_calls[0]["args"]
pydantic_object = ResponseFormatter.model_validate(tool_call_args)

print(pydantic_object)