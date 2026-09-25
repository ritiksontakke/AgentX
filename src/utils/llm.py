from  langchain.agents import create_agent
from  dotenv import load_dotenv
import os


load_dotenv()

def openai():
    return create_agent(
        model="openai:gpt-5.5",
        api_key = os.getenv("OPENAI_API_KEY")
    )

def AiModel():
    return openai()