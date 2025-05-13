from typing import Annotated
from langchain_core.tools import tool
from langchain_openai import AzureChatOpenAI
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# ✅ Create tool with description, so it works with OpenAI schema
@tool
def user_specific_tool(
    input_data: str,
    user_id: Annotated[str, "User ID to associate with this operation"]
) -> str:
    """Tool that processes input for a specific user."""
    return f"User {user_id} processed: {input_data}"

# ✅ Chat model setup
chat = AzureChatOpenAI(
    temperature=0,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2023-07-01"
)

# ✅ Bind tool to LLM
chat_with_tools = chat.bind_tools([user_specific_tool])

# ✅ Messages
messages = [
    SystemMessage(content="You are a secure assistant. You never ask for user ID."),
    HumanMessage(content="Process the file called 'confidential_notes.txt'")
]

# ✅ Inject `user_id` at runtime
config = RunnableConfig(configurable={"user_id": "user_456"})

# ✅ LLM chooses tool, we inject hidden value
response = chat_with_tools.invoke(messages, config=config)

print("\n Assistant Response:")
print(response.content)
