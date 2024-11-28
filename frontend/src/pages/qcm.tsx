import { useState } from 'react';
import { MathJax, MathJaxContext } from 'better-react-mathjax';
import axios from 'axios';

const QCMApp = () => {
  // Sample QCM data with LaTeX support
  const qcmData = [
    {
      question: "What is the quadratic formula for solving $ax^2 + bx + c = 0$?",
      options: [
        "$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$",
        "$x = \\frac{-b + \\sqrt{b^2 + 4ac}}{2a}$",
        "$x = \\frac{b \\pm \\sqrt{b^2 - 4ac}}{2a}$",
        "$x = \\frac{b + \\sqrt{b^2 + 4ac}}{2a}$"
      ]
    },
    {
      question: "What is the derivative of $f(x) = x^2$?",
      options: [
        "$f'(x) = 2x$",
        "$f'(x) = x$",
        "$f'(x) = 3x^2$",
        "$f'(x) = 0$"
      ]
    },
    {
      question: "Evaluate the integral $\\int_0^1 x^2 dx$",
      options: [
        "$\\frac{1}{2}$",
        "$\\frac{1}{3}$", 
        "$1$",
        "$\\frac{2}{3}$"
      ]
    }
  ];

  // State to track selected answers and submission
  const [selectedAnswers, setSelectedAnswers] = useState(
    new Array(qcmData.length).fill(null)
  );
  const [submitted, setSubmitted] = useState(false);

  // Handler for selecting an answer
  const handleAnswerSelect = (questionIndex: any, optionIndex: any) => {
    const newSelectedAnswers = [...selectedAnswers];
    newSelectedAnswers[questionIndex] = optionIndex;
    setSelectedAnswers(newSelectedAnswers);
  };

  // Handler for submission
  const handleSubmit = async () => {
    setSubmitted(true);
  
    try {
      const response = await axios.post('http://127.0.0.1:5000/submit', {
        answers: selectedAnswers,
      });
  
      console.log('Server response:', response.data);
    } catch (error) {
      console.error('Error submitting answers:', error);
    }
  };

  // Configuration for MathJax
  const config = {
    loader: { load: ["input/tex", "output/chtml"] },
    tex: { inlineMath: [["$", "$"], ["\\(", "\\)"]] },
  };

  return (
    <MathJaxContext config={config}>
      <div className="max-w-2xl mx-auto p-6 bg-white shadow-md rounded-lg">
        <h1 className="text-2xl font-bold mb-6 text-center">Mathematics QCM</h1>
        
        {qcmData.map((item, questionIndex) => (
          <div key={questionIndex} className="mb-6">
            <MathJax>
              <p className="font-semibold mb-3">{`${questionIndex + 1}. ${item.question}`}</p>
            </MathJax>
            
            <div className="space-y-2">
              {item.options.map((option, optionIndex) => (
                <label 
                  key={optionIndex} 
                  className={`block p-3 border rounded cursor-pointer transition-colors 
                    ${selectedAnswers[questionIndex] === optionIndex 
                      ? 'bg-blue-100 border-blue-500' 
                      : 'hover:bg-gray-100'}
                    ${submitted && selectedAnswers[questionIndex] === null 
                      ? 'border-red-300' 
                      : ''}`}
                >
                  <input
                    type="radio"
                    name={`question-${questionIndex}`}
                    className="mr-3"
                    checked={selectedAnswers[questionIndex] === optionIndex}
                    onChange={() => handleAnswerSelect(questionIndex, optionIndex)}
                  />
                  <MathJax>{option}</MathJax>
                </label>
              ))}
            </div>
          </div>
        ))}
        
        <button 
          onClick={handleSubmit}
          disabled={selectedAnswers.some(answer => answer === null)}
          className={`w-full py-3 rounded text-white font-bold transition-colors 
            ${selectedAnswers.some(answer => answer === null)
              ? 'bg-gray-400 cursor-not-allowed'
              : 'bg-blue-600 hover:bg-blue-700 active:bg-blue-800'}`}
        >
          Submit Answers
        </button>

        {submitted && (
          <div className="mt-6 p-4 bg-green-100 border-l-4 border-green-500">
            <p className="font-semibold">Answers submitted successfully!</p>
            <div className="mt-2">
              {selectedAnswers.map((answer, index) => (
                <p key={index}>
                  Question {index + 1}: Option {answer + 1}
                </p>
              ))}
            </div>
          </div>
        )}
      </div>
    </MathJaxContext>
  );
};

export default QCMApp;
