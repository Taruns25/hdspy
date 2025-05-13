import os
from langchain_community.chat_models import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationTokenBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.llms import OpenAI
from dotenv import load_dotenv , find_dotenv
import warnings

warnings.filterwarnings('ignore')

load_dotenv(find_dotenv())

temperature = 0.0

# Setup Azure OpenAI model
llm_model = os.getenv("AZURE_OPENAI_DEPLOYMENT")
chat = AzureChatOpenAI(
    temperature=temperature,
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-05-15",
    deployment_name=llm_model
)

#memory = ConversationBufferMemory()
# memory = ConversationBufferWindowMemory(k=1)
memory = ConversationSummaryBufferMemory(llm=chat, max_token_limit=400)
# memory.save_context({"input": "AI is what?!"},
#                     {"output": "Amazing!"})
# memory.save_context({"input": "Backpropagation is what?"},
#                     {"output": "Beautiful!"})
# memory.save_context({"input": "Chatbots are what?"}, 
#                     {"output": "Charming!"})

conversation = ConversationChain(
    llm=chat, 
    memory = memory,
    verbose=True
)
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=chat, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"}, 
                    {"output": f"{schedule}"})


x=memory.load_memory_variables({})
print(x)
print(conversation.predict(input="What would be a good demo to show?")) 
# print(conversation.predict(input="Hello this is anon"))
# print(conversation.predict(input="whats my 1+1?"))
# print(conversation.predict(input="whats my name?"))
# # memory.save_context({"input":"Hello"},{"output":"whats good ?"})