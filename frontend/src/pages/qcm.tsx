import { useState } from 'react';
import { MathJax, MathJaxContext } from 'better-react-mathjax';
import axios from 'axios';
import { useAppContext } from "./AppContext";



const QCMApp = () => {
    const { qcmData} = useAppContext();

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

            console.log('Server response:', response.data);
        } catch (error) {
            console.error('Error submitting answers:', error);
        }
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

                        {section.content.map((item: any, questionIndex: any) => (
                            <div key={questionIndex} className="mb-6">
                                <MathJax>
                                    <p className="font-semibold mb-3">{`${questionIndex + 1}. ${item.question}`}</p>
                                </MathJax>

                                <div className="space-y-2">
                                    {item.options.map((option: any, optionIndex: any) => (
                                        <label
                                            key={optionIndex}
                                            className={`block p-3 border rounded cursor-pointer transition-colors 
                        ${selectedAnswers[sectionIndex].answers[questionIndex] === optionIndex
                                                    ? 'bg-blue-100 border-blue-500'
                                                    : 'hover:bg-gray-100'
                                                }
                        ${submitted &&
                                                    selectedAnswers[sectionIndex].answers[questionIndex] === null
                                                    ? 'border-red-300'
                                                    : ''
                                                }`}
                                        >
                                            <input
                                                type="radio"
                                                name={`question-${sectionIndex}-${questionIndex}`}
                                                className="mr-3"
                                                checked={
                                                    selectedAnswers[sectionIndex].answers[questionIndex] === optionIndex
                                                }
                                                onChange={() =>
                                                    handleAnswerSelect(sectionIndex, questionIndex, optionIndex)
                                                }
                                            />
                                            <MathJax>{option}</MathJax>
                                        </label>
                                    ))}
                                </div>
                            </div>
                        ))}
                    </div>
                ))}

                <button
                    onClick={handleSubmit}
                    disabled={selectedAnswers.some(section =>
                        section.answers.some(answer => answer === null)
                    )}
                    className={`w-full py-3 rounded text-white font-bold transition-colors 
            ${selectedAnswers.some(section =>
                        section.answers.some(answer => answer === null)
                    )
                            ? 'bg-gray-400 cursor-not-allowed'
                            : 'bg-blue-600 hover:bg-blue-700 active:bg-blue-800'}`}
                >
                    Submit Answers
                </button>

                {submitted && (
                    <div className="mt-6 p-4 bg-green-100 border-l-4 border-green-500">
                        <p className="font-semibold">Answers submitted successfully!</p>
                        <div className="mt-2">
                            {selectedAnswers.map((section, sectionIndex) => (
                                <div key={sectionIndex}>
                                    <p className="font-bold">{section.sous_cours_name}</p>
                                    {section.answers.map((answer, questionIndex) => (
                                        <p key={questionIndex}>
                                            Question {questionIndex + 1}: Option {answer + 1}
                                        </p>
                                    ))}
                                </div>
                            ))}
                        </div>
                    </div>
                )}
            </div>
        </MathJaxContext>
    );
};

export default QCMApp;
