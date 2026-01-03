import requests
import os
from dotenv import load_dotenv
from systemprompt import SYSTEM_PROMPT
# load env 
load_dotenv()

GROQ_API_KEY = os.getenv("groq_api_key")

BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"   


def groq_chat(message, system_prompt=SYSTEM_PROMPT):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        "temperature": 0.3,
        "max_tokens": 300
    }

    response = requests.post(BASE_URL, headers=headers, json=data)
    
    response.raise_for_status()
    out = response.json()

    return out["choices"][0]["message"]["content"]

