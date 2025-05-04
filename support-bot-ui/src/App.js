// src/App.js

import React, { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Replace with your backend URL or OpenRouter API
      const response = await axios.post("http://127.0.0.1:8000/generate", {
        question: question,
      });

      // Assuming the response contains an answer field
      setAnswer(response.data.response);
    } catch (err) {
      setError("Error fetching answer. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Question and Answer</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="question">Ask a Question: </label>
          <input
            type="text"
            id="question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Enter your question here"
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? "Asking..." : "Ask"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {answer && (
        <div>
          <h2>Answer:</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
