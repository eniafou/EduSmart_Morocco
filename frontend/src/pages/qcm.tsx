import { useState } from 'react';
import { MathJax, MathJaxContext } from 'better-react-mathjax';
import axios from 'axios';
import { useAppContext } from "./AppContext";
import { useNavigate } from "react-router-dom"; // Assuming react-router-dom is being used for navigation

const QCMApp = () => {
    const { qcmData, setCustomizedCourse } = useAppContext(); // Assuming `setCustomizedCourse` is part of AppContext
    const navigate = useNavigate();

    if (!qcmData || qcmData.length === 0) {
        return <p>No QCM data available. Go back and generate questions first.</p>;
    }

    const [selectedAnswers, setSelectedAnswers] = useState(
        qcmData.map(section => ({
            sous_cours_name: section.sous_cours_name,
            answers: new Array(section.content.length).fill(null),
        }))
    );

    const [submitted, setSubmitted] = useState(false);
    const [submitLabel, setSubmitLabel] = useState("Submit Answers");

    const handleAnswerSelect = (sectionIndex: number, questionIndex: number, optionIndex: number) => {
        const newSelectedAnswers = [...selectedAnswers];
        newSelectedAnswers[sectionIndex].answers[questionIndex] = optionIndex;
        setSelectedAnswers(newSelectedAnswers);
    };

    const handleSubmit = async () => {
        setSubmitted(true);

        try {
            const response = await axios.post('http://127.0.0.1:5000/submit', {
                answers: selectedAnswers,
                qcm: qcmData,
            });

            // Set the customized course data in the app context
            setCustomizedCourse(response.data["cours"]);
            setSubmitLabel("Get your customized course");
        } catch (error) {
            console.error('Error submitting answers:', error);
        }
    };

    const handleRedirect = () => {
        navigate("/customized-course"); // Redirect to the new page
    };

    const config = {
        loader: { load: ['input/tex', 'output/chtml'] },
        tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
    };

    return (
        <MathJaxContext config={config}>
            <div className="max-w-3xl mx-auto p-6 bg-white shadow-md rounded-lg">
                <h1 className="text-2xl font-bold mb-6 text-center">Mathematics QCM</h1>

                {qcmData.map((section, sectionIndex) => (
                    <div key={sectionIndex} className="mb-8">
                        <h2 className="text-xl font-bold mb-4">{section.sous_cours_name}</h2>

                        {section.content.map((item, questionIndex) => {
                            const userAnswer = selectedAnswers[sectionIndex].answers[questionIndex];
                            const correctAnswer = item.options.findIndex(
                                option => option.startsWith(item.correct_answer)
                            );

                            return (
                                <div key={questionIndex} className="mb-6">
                                    <MathJax>
                                        <p className="font-semibold mb-3">{`${questionIndex + 1}. ${item.question}`}</p>
                                    </MathJax>

                                    <div className="space-y-2">
                                        {item.options.map((option, optionIndex) => (
                                            <label
                                                key={optionIndex}
                                                className={`block p-3 border rounded cursor-pointer transition-colors 
                        ${
                            submitted
                                ? optionIndex === correctAnswer
                                    ? 'bg-green-100 border-green-500'
                                    : optionIndex === userAnswer && userAnswer !== correctAnswer
                                    ? 'bg-red-100 border-red-500'
                                    : ''
                                : selectedAnswers[sectionIndex].answers[questionIndex] === optionIndex
                                ? 'bg-blue-100 border-blue-500'
                                : 'hover:bg-gray-100'
                        }`}
                                            >
                                                <input
                                                    type="radio"
                                                    name={`question-${sectionIndex}-${questionIndex}`}
                                                    className="mr-3"
                                                    checked={userAnswer === optionIndex}
                                                    onChange={() =>
                                                        handleAnswerSelect(sectionIndex, questionIndex, optionIndex)
                                                    }
                                                />
                                                <MathJax>{option}</MathJax>
                                            </label>
                                        ))}
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                ))}

                <button
                    onClick={submitted ? handleRedirect : handleSubmit}
                    disabled={!submitted && selectedAnswers.some(section =>
                        section.answers.some(answer => answer === null)
                    )}
                    className={`w-full py-3 rounded text-white font-bold transition-colors 
            ${!submitted && selectedAnswers.some(section =>
                        section.answers.some(answer => answer === null)
                    )
                            ? 'bg-gray-400 cursor-not-allowed'
                            : 'bg-blue-600 hover:bg-blue-700 active:bg-blue-800'}`}
                >
                    {submitLabel}
                </button>
            </div>
        </MathJaxContext>
    );
};

export default QCMApp;
