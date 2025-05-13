# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage, ToolCall
# from langchain_openai import AzureChatOpenAI  # ✅ New import
# import os
# from dotenv import load_dotenv, find_dotenv

# # Load .env
# load_dotenv(find_dotenv())

# chat = AzureChatOpenAI(
#     temperature=0.0,
#     deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
#     api_key=os.getenv("AZURE_OPENAI_KEY"),
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     api_version="2023-05-15"
# )

# # Step 1: Setup messages
# system_msg = SystemMessage(content="You are a helpful assistant.")
# user_msg = HumanMessage(content="What's the weather in Bangalore?")

# # Step 2: Simulate assistant making a tool call
# tool_call = ToolCall(
#     name="get_weather",
#     args={"city": "Bangalore"},  #  dict, not string
#     id="weather_tool_1"
# )

# assistant_msg = AIMessage(
#     content="Let me check the weather...",
#     tool_calls=[tool_call]
# )

# # Step 3: Simulate tool response
# tool_response = ToolMessage(
#     content='{"temperature": "27°C", "condition": "sunny"}',
#     tool_call_id="weather_tool_1"
# )

# # Step 4: Final response from assistant
# response = chat.invoke([
#     system_msg,
#     user_msg,
#     assistant_msg,
#     tool_response
# ])

# print("\nFinal Assistant Response:", response.content)
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_openai import AzureChatOpenAI
from langchain_core.tools import tool
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

chat = AzureChatOpenAI(
    temperature=0.0,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2023-05-15"
)

@tool
def get_weather(city: str) -> str:
    """Returns weather information for a city."""
    return f"The weather in {city} is 27°C and sunny."

tools = [get_weather]
model_with_tools = chat.bind_tools(tools)

system_msg = SystemMessage(
    content="You are a helpful assistant. If the user asks about weather, always use the get_weather tool."
)

user_msg = HumanMessage(content="What's the weather in Bangalore?")

initial_response = model_with_tools.invoke([system_msg, user_msg])

if initial_response.tool_calls:
    print("\nTool call detected:", initial_response.tool_calls)
    
    tool_call = initial_response.tool_calls[0]
    tool_name = tool_call['name']
    tool_args = tool_call['args']
    tool_call_id = tool_call['id']

    if tool_name == "get_weather":
        tool_result = get_weather.invoke(tool_args)
    else:
        tool_result = "Tool not recognized."

    tool_response = ToolMessage(
        content=json.dumps({"result": tool_result}),
        tool_call_id=tool_call_id
    )

    final_response = model_with_tools.invoke([
        system_msg,
        user_msg,
        initial_response,
        tool_response
    ])

    print("\nFinal Assistant Response:", final_response.content)

else:
    print("\nNo tool call detected. Model responded with:\n", initial_response.content)


