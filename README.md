# 🤖 GenAI Support Bot

A simple Q&A web application using a React frontend and FastAPI backend powered by a GenAI model (like `microsoft/phi-4-reasoning-plus`) via OpenRouter.

---

## 🚀 Features

- Ask any question via a simple web UI
- Uses a GenAI model to generate answers
- FastAPI backend handles GenAI API calls
- Axios-based communication between frontend and backend
- CORS-enabled API for cross-origin access

---

## 🧱 Project Structure

```
genai-support-bot/
│
├── backend/
│   └── genai_app.py        # FastAPI backend with /generate endpoint
│
├── frontend/
│   ├── src/
│   │   ├── App.js          # React component with Q&A logic
│   │   └── index.js        # Entry point for React
│   └── package.json        # React metadata and dependencies
│
└── README.md               # This file
```

---

## ⚙️ Setup Instructions

### 🖥 Backend (FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install fastapi uvicorn requests
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn genai_app:app --reload
   ```

> Default server runs on `http://127.0.0.1:8000`

---

### 🌐 Frontend (React)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React app:
   ```bash
   npm start
   ```

> App runs at `http://localhost:3000`

---

## 🔁 API Endpoint

### `POST /generate`

**Request Body:**
```json
{
  "question": "What is AI?"
}
```

**Response:**
```json
{
  "response": "AI stands for Artificial Intelligence..."
}
```

---

## 🛠 Technologies Used

- **React** (Frontend)
- **FastAPI** (Backend)
- **Axios** (HTTP requests)
- **OpenRouter / GenAI API** (AI-powered Q&A)
- **CORS Middleware** (Cross-origin support)

---

## ❗ Troubleshooting

- **CORS Error**: Make sure FastAPI has CORS middleware enabled:
  ```python
  from fastapi.middleware.cors import CORSMiddleware
  ```

- **405 OPTIONS Method Not Allowed**: Ensure preflight requests are handled in backend.

- **Unprocessable Entity (422)**: Check your frontend JSON structure and backend Pydantic model.

---

## 📌 Future Enhancements

- Add chat history
- Enable streaming responses
- Deploy frontend (e.g., Vercel) and backend (e.g., Render or Fly.io)

---

## 📜 License

MIT License – Feel free to use, modify, and distribute.

---

## 🙌 Acknowledgments

- [OpenRouter.ai](https://openrouter.ai) for GenAI API
- [FastAPI](https://fastapi.tiangolo.com)
- [Create React App](https://create-react-app.dev)