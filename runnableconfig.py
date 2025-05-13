from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.config import RunnableConfig

# Define a simple function
def greet(name):
    return f"Hello, {name}!"

# Wrap in a Runnable
runnable = RunnableLambda(greet)

# Define configuration(this is optional)
config = RunnableConfig(
    run_name="greet_run",
    tags=["greeting", "demo"],
    metadata={"called_by": "user"}
)

# Run it
output = runnable.invoke("user", config=config)
print(output) 


