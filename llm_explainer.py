# llm_explainer.py

import os
from dotenv import load_dotenv  # load .env variables
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Example: Ask a question to a GPT model
prompt = """
Explain in simple terms how IoT sensor fault prediction works in industrial networks.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
)

# Print the response
print(response.choices[0].message.content)
