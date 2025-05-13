from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Setup Azure OpenAI model
llm_model = os.getenv("AZURE_OPENAI_DEPLOYMENT")
chat = AzureChatOpenAI(
    temperature=0.7,
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-05-15",
    deployment_name=llm_model
)

# Sample unstructured customer review text
customer_review = """\
This leaf blower is pretty amazing. It has four settings: candle blower, gentle breeze, windy city, and tornado.
It arrived in two days, just in time for my wife's anniversary present.
I think my wife liked it so much she was speechless.
So far I've been the only one using it, and I've been using it every other morning to clear the leaves on our lawn.
It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features.
"""

# Define the expected output schema
gift_schema = ResponseSchema(
    name="gift",
    description="Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown."
)

delivery_days_schema = ResponseSchema(
    name="delivery_days",
    description="How many days did it take for the product to arrive? If not found, output -1."
)

price_value_schema = ResponseSchema(
    name="price_value",
    description="Extract any sentences about the value or price, and output them as a JSON list of strings."
)

# Build the structured output parser
response_schemas = [gift_schema, delivery_days_schema, price_value_schema]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

# Create prompt template
review_template = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price, and output them as a JSON list of strings.

text: {text}

{format_instructions}

Only return valid JSON.
Ensure lists are actual JSON arrays (not strings).
Do not include comments or explanations.
"""

# Format prompt with the input and formatting instructions
prompt = ChatPromptTemplate.from_template(review_template)
messages = prompt.format_messages(
    text=customer_review,
    format_instructions=format_instructions
)

# Send prompt to LLM and parse response
response = chat.invoke(messages)
output = output_parser.parse(response.content)

# Display the structured result
print("\nExtracted Structured Data:\n")
print(output)
