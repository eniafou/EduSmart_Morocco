import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

type Level = "lycee" | "college" | "primaire";
type Difficulty = "Facile" | "Moyen" | "Difficile";

interface FormData {
  level: Level | "";
  year: string | "";
  branch: string;
  subject: string;
  lesson: string;
  difficulty: Difficulty | "";
  num_questions: number;
}

const GeneralQCMForm = ({ setQcmData }: { setQcmData: (data: any) => void }) => {
  const navigate = useNavigate();
  const [step, setStep] = useState<number>(1);
  const [loading, setLoading] = useState<boolean>(false);
  const [formData, setFormData] = useState<FormData>({
    level: "",
    year: "",
    branch: "",
    subject: "math",
    lesson: "notion_de_logique",
    difficulty: "",
    num_questions: 1,
  });

  const levels: Level[] = ["lycee", "college", "primaire"];
  const years: Record<Level, string[]> = {
    lycee: ["tronc_commun", "1_bac", "2_bac"],
    college: ["Year 4", "Year 5", "Year 6"],
    primaire: ["Year 7", "Year 8", "Year 9"],
  };
  const branches: Record<Level, Record<string, string[]>> = {
    lycee: {
      "1_bac": ["sci_math", "sci_exp"],
      "2_bac": ["Branch C", "Branch D"],
      "tronc_commun": [],
    },
    college: {
      "Year 4": [],
      "Year 5": [],
      "Year 6": [],
    },
    primaire: {
      "Year 7": [],
      "Year 8": [],
      "Year 9": [],
    },
  };
  const difficulties: Difficulty[] = ["Facile", "Moyen", "Difficile"];

  const handleNext = () => setStep((prev) => Math.min(prev + 1, 7));
  const handlePrev = () => setStep((prev) => Math.max(prev - 1, 1));

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/create_general_qcm",
        formData
      );
      setQcmData(response.data);
      navigate("/qcm");
    } catch (error) {
      console.error("Error submitting answers:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleChange = <K extends keyof FormData>(key: K, value: FormData[K]) => {
    setFormData({ ...formData, [key]: value });
  };

  const renderStep = () => {
    switch (step) {
      case 1:
        return (
          <div>
            <label className="block text-lg font-semibold">Select Level</label>
            <select
              className="w-full mt-2 p-2 border rounded"
              value={formData.level}
              onChange={(e) => handleChange("level", e.target.value as Level)}
            >
              <option value="" disabled>
                Choose Level
              </option>
              {levels.map((level) => (
                <option key={level} value={level}>
                  {level}
                </option>
              ))}
            </select>
          </div>
        );
      case 2:
        return (
          <div>
            <label className="block text-lg font-semibold">Select Year</label>
            <select
              className="w-full mt-2 p-2 border rounded"
              value={formData.year}
              onChange={(e) => handleChange("year", e.target.value)}
              disabled={!formData.level}
            >
              <option value="" disabled>
                Choose Year
              </option>
              {formData.level &&
                years[formData.level].map((year) => (
                  <option key={year} value={year}>
                    {year}
                  </option>
                ))}
            </select>
          </div>
        );
      case 3:
        return (
          <div>
            <label className="block text-lg font-semibold">Select Branch</label>
            <select
              className="w-full mt-2 p-2 border rounded"
              value={formData.branch}
              onChange={(e) => handleChange("branch", e.target.value)}
              disabled={!formData.level || !formData.year}
            >
              <option value="" disabled>
                Choose Branch
              </option>
              {formData.level &&
                formData.year &&
                branches[formData.level][formData.year]?.map((branch) => (
                  <option key={branch} value={branch}>
                    {branch}
                  </option>
                ))}
            </select>
          </div>
        );
      case 4:
        return (
          <div>
            <label className="block text-lg font-semibold">Enter Subject</label>
            <input
              type="text"
              className="w-full mt-2 p-2 border rounded"
              placeholder="Enter subject"
              value={formData.subject}
              onChange={(e) => handleChange("subject", e.target.value)}
            />
          </div>
        );
      case 5:
        return (
          <div>
            <label className="block text-lg font-semibold">Enter Lesson</label>
            <input
              type="text"
              className="w-full mt-2 p-2 border rounded"
              placeholder="Enter lesson"
              value={formData.lesson}
              onChange={(e) => handleChange("lesson", e.target.value)}
            />
          </div>
        );
      case 6:
        return (
          <div>
            <label className="block text-lg font-semibold">Select Difficulty</label>
            <select
              className="w-full mt-2 p-2 border rounded"
              value={formData.difficulty}
              onChange={(e) =>
                handleChange("difficulty", e.target.value as Difficulty)
              }
            >
              <option value="" disabled>
                Choose Difficulty
              </option>
              {difficulties.map((difficulty) => (
                <option key={difficulty} value={difficulty}>
                  {difficulty}
                </option>
              ))}
            </select>
          </div>
        );
      case 7:
        return (
          <div>
            <label className="block text-lg font-semibold">
              Number of Questions
            </label>
            <input
              type="number"
              className="w-full mt-2 p-2 border rounded"
              value={formData.num_questions}
              onChange={(e) =>
                handleChange(
                  "num_questions",
                  Math.min(Math.max(+e.target.value, 1), 10)
                )
              }
              min={1}
              max={10}
            />
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div
      className="min-h-screen bg-gradient-to-br from-blue-100 to-white flex justify-center items-center"
    >
      <div className="bg-white shadow-lg rounded-lg p-8 max-w-lg w-full">
        {/* Progress Bar */}
        <div className="relative mb-6">
          <div className="absolute top-0 left-0 h-2 bg-gray-300 w-full"></div>
          <div
            className="absolute top-0 left-0 h-2 bg-blue-600"
            style={{ width: `${(step / 7) * 100}%` }}
          ></div>
        </div>

        <h1 className="text-3xl font-bold text-gray-800 mb-6">Step {step}</h1>
        {renderStep()}
        <div className="flex justify-between mt-8">
          <button
            className="px-6 py-3 bg-gray-300 rounded-md text-lg text-gray-700 hover:bg-gray-400 disabled:bg-gray-200"
            disabled={step === 1}
            onClick={handlePrev}
          >
            &larr; Previous
          </button>
          {step === 7 ? (
            <button
              className={`px-6 py-3 rounded-md text-lg ${loading
                  ? "bg-gray-400 cursor-not-allowed"
                  : "bg-blue-600 text-white hover:bg-blue-700"
                }`}
              onClick={handleSubmit}
              disabled={loading} // Disable button while loading
            >
              {loading ? (
                <div className="flex items-center">
                  <svg
                    className="animate-spin h-5 w-5 text-white mr-2"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                    ></circle>
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8v8H4z"
                    ></path>
                  </svg>
                  Loading...
                </div>
              ) : (
                "Submit"
              )}
            </button>
          ) : (
            <button
              className="px-6 py-3 bg-blue-600 text-white rounded-md text-lg hover:bg-blue-700"
              onClick={handleNext}
              disabled={
                (step === 2 && !formData.year) || (step === 3 && !formData.branch.length)
              }
            >
              Next
            </button>
          )}
        </div>
      </div>
    </div>
  );

};

export default GeneralQCMForm;
