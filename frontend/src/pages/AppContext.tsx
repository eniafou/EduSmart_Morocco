import React, { createContext, useContext, useState, ReactNode } from "react";
import {FormData, QCMData} from "../types/types"
// Define types for Level, Difficulty, and FormData


// Define the context type
interface AppContextType {
  qcmData: QCMData; // Replace `any` with a more specific type if possible
  setQcmData: React.Dispatch<React.SetStateAction<QCMData>>;
  formData: FormData;
  setFormData: React.Dispatch<React.SetStateAction<FormData>>;
  customizedCourse: string;
  setCustomizedCourse: React.Dispatch<React.SetStateAction<string>>;
}

// Define default values for formData
const defaultFormData: FormData = {
    level: "Lycée",
    year: "1ère Bac",
    branch: "Sciences Mathématiques",
    subject: "Mathématiques",
    lesson: "Notion de logique",
    difficulty: "Moyen",
    num_questions: 1,
  };
  
  // Define default values for qcmData (assuming it's an empty array by default)
  const defaultQcmData: QCMData = [];
  
  // Create the context with default values
  const AppContext = createContext<AppContextType>({
    qcmData: defaultQcmData,
    setQcmData: () => {}, // Default is a no-op function
    formData: defaultFormData,
    setFormData: () => {}, // Default is a no-op function
    customizedCourse: "",
    setCustomizedCourse: () => {}, // Default is a no-op function
  });



// Provider component
export const AppProvider = ({ children }: { children: ReactNode }) => {
  // State for QCM data
  const [qcmData, setQcmData] = useState<QCMData>([]);

  // State for form data
  const [formData, setFormData] = useState<FormData>(defaultFormData);
  const [customizedCourse, setCustomizedCourse] = useState<string>("");

  return (
    <AppContext.Provider value={{ qcmData, setQcmData, formData, setFormData, customizedCourse, setCustomizedCourse}}>
      {children}
    </AppContext.Provider>
  );
};

// Custom hook to use the context
export const useAppContext = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error("useAppContext must be used within a AppProvider");
  }
  return context;
};
