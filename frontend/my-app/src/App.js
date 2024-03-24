import { Main, Image, Sentimental, Instagram, Report } from "./index";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/image" element={<Image />} />
        <Route path="/sentiment" element={<Sentimental />} />
        <Route path="/instagram" element={<Instagram />} />
        <Route path="/report" element={<Report />} />
      </Routes>
    </Router>
  );
}

export default App;
