import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Set OpenRouter configuration
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

# You can change this to other models like gpt-4 or mistral too
MODEL = "qwen:Qwen1.5-7B-Chat"

def chat_with_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()