import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import QCMApp from "./pages/qcm";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<QCMApp />} />
        {/* <Route path="/about" element={<AboutPage />} />
        <Route path="/contact" element={<ContactPage />} /> */}
      </Routes>
    </Router>
  );
};

export default App;
