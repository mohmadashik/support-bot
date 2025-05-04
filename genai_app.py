from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()  # Load OPENROUTER_API_KEY from .env

app = FastAPI()

# Allow your frontend origin (adjust if hosted elsewhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class PromptInput(BaseModel):
    question: str

async def call_openrouter(prompt: str):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",  # Optional for OpenRouter tracking
        "X-Title": "FastAPI-GenAI-App",           # Optional
    }

    payload = {
        "model": "microsoft/phi-4-reasoning-plus:free",
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "temperature": 0.7,
                "top_p": 0.9,
                "max_tokens": 200,
                "stop": ["\n", "\n"],
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "n": 1,
                "stream": False,

            }
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=headers,
                             data=json.dumps(payload))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.text)

    data = response.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Invalid response format from OpenRouter")

@app.post("/generate")
async def generate(input: PromptInput):
    result = await call_openrouter(input.question)
    return {"response": result}
