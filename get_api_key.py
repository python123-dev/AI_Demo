import os

from dotenv import load_dotenv


def get_api_key():
    """Return the OpenAI API key from the environment or the local .env file."""
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
