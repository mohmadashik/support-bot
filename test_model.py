import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "microsoft/phi-4-reasoning-plus:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?",
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 100,
        "stop": ["\n", "\n"],
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "n": 1,
        "stream": False,
        
      }
    ],
    
  })
)
print(response.status_code)
print(response.json())