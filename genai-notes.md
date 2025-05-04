# GenAI Learning Notes – [Date: 2025-05-04]

## ✅ Topics Covered

### 1. GenAI Parameters in API Calls
- **`model`**: Specifies the AI model to use (e.g., `microsoft/phi-4-reasoning-plus:free`)
- **`temperature`**: Controls randomness. Lower = more deterministic.
- **`max_tokens`**: Limits the response length.
- **`top_p`**: Controls diversity. 1.0 = full range sampling.
- **`frequency_penalty`**: Penalizes repeating phrases.
- **`presence_penalty`**: Encourages new topics in responses.
- **`stop`**: Defines where the response should stop.
- **`stream`**: Enables response streaming.
- **`n`**: Number of responses to generate.

> ✅ These parameters are mostly consistent across different models on OpenRouter or similar GenAI platforms.

---

### 2. FastAPI Backend Setup
- Created a simple FastAPI app with a `/generate` POST endpoint to process questions and return AI-generated answers.
- Used CORS middleware to allow frontend access.

**Common Errors & Fixes**
- `NameError: name 'CORSMiddleware' is not defined` → ✅ Fixed by importing:
  ```python
  from fastapi.middleware.cors import CORSMiddleware
