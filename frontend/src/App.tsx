import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import QCMApp from "./pages/qcm";
import GeneralQCMForm from "./pages/GeneralQCMForm";
import { AppProvider } from "./pages/AppContext";







const App = () => {
  return (
    <AppProvider>
    <Router>
      <Routes>
        {/* Root Page */}
        <Route path="/" element={<GeneralQCMForm/>} />
        
        {/* QCM Page */}
        <Route path="/qcm" element={<QCMApp />} />
      </Routes>
    </Router>
    </AppProvider>
  );
};

export default App;