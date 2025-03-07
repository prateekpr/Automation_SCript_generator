from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def generate_script(prompt):
    # Get the Grok API key from environment variables
    api_key = os.getenv("GROK_API_KEY")
    if not api_key:
        raise ValueError("Grok API key not found in environment variables.")

    # Initialize ChatGroq client
    chat = ChatGroq(api_key=api_key, model_name="mixtral-8x7b-32768")  # Replace with the correct model name

    # Create a HumanMessage object with the prompt
    message = HumanMessage(content=prompt)

    # Generate a response using the chat model
    response = chat.invoke([message])  # Use invoke instead of __call__

    # Return the generated text
    return response.content