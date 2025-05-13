from langchain_core.runnables import RunnableLambda
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

# Step 1: Initialize the Chat Model
chat = AzureChatOpenAI(
     temperature=0.0,
     deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
     api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-08-01-preview"
)

# Step 2: Define Runnable A: Translate to French
A = RunnableLambda(lambda x: [HumanMessage(content=f"Translate to English US: {x}")]) | chat

# Step 3: Define Runnable B: Summarize
B = RunnableLambda(lambda x: [HumanMessage(content=f"Summarize: {x.content}")]) | chat

# Step 4: Compose the pipeline
pipeline = A | B

# Step 5: Run .invoke()
output = pipeline.invoke("LangChain is awesome.")
print("USING .invoke():", output.content)

# Step 6: Run .batch()
batch_inputs = [
    "LangChain is great for LLM apps.",
    "OpenAI models are widely used.",
    "Python is a versatile language."
]
batch_results = pipeline.batch(batch_inputs)
print("\n USING .batch():")
for res in batch_results:
    print("-", res.content)

# Step 7: Run .stream()
print("\n USING .stream():")
for chunk in pipeline.stream("LangChain speeds up prototyping."):
    print(chunk.content, end="", flush=True)
print()
