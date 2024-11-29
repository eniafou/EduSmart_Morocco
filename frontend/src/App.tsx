import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import QCMApp from "./pages/qcm";
import { useState } from "react";
import GeneralQCMForm from "./pages/GeneralQCMForm";






const App = () => {
  // State to store qcmData
  const [qcmData, setQcmData] = useState([]);

  return (
    <Router>
      <Routes>
        {/* Root Page */}
        <Route path="/" element={<GeneralQCMForm setQcmData={setQcmData}/>} />
        
        {/* QCM Page */}
        <Route path="/qcm" element={<QCMApp qcmData={qcmData} />} />
      </Routes>
    </Router>
  );
};

export default App;