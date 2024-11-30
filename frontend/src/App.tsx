import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import QCMApp from "./pages/qcm";
import GeneralQCMForm from "./pages/GeneralQCMForm";
import { AppProvider } from "./pages/AppContext";
import CustomizedLesson from "./pages/CustomizedLesson";







const App = () => {
  return (
    <AppProvider>
    <Router>
      <Routes>
        <Route path="/" element={<GeneralQCMForm/>} />
        <Route path="/qcm" element={<QCMApp />} />
        <Route path="/customized-course" element={<CustomizedLesson />} />
        <Route path="/customized-qcm" element={<CustomizedLesson />} />
      </Routes>
    </Router>
    </AppProvider>
  );
};

export default App;