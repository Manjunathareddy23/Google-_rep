import React, { useState } from 'react';
import axios from 'axios';

function TeachingAssistant() {
  const [studentInput, setStudentInput] = useState('');
  const [socraticQuestion, setSocraticQuestion] = useState('');

  const handleAsk = async () => {
    try {
      const response = await axios.post('http://localhost:5000/ask', { input: studentInput });
      setSocraticQuestion(response.data.socratic_question);
    } catch (error) {
      console.error('Error asking question:', error);
    }
  };

  return (
    <div>
      <h1>Socratic Teaching Assistant</h1>
      <input
        type="text"
        value={studentInput}
        onChange={(e) => setStudentInput(e.target.value)}
        placeholder="Enter your problem..."
      />
      <button onClick={handleAsk}>Ask</button>

      {socraticQuestion && (
        <div>
          <h2>Socratic Question:</h2>
          <p>{socraticQuestion}</p>
        </div>
      )}
    </div>
  );
}

export default TeachingAssistant;
