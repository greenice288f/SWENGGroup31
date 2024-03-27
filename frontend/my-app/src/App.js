import { Main, Image, Sentimental, Instagram, Report } from "./index";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Button from "./components/Button";
import AgreementPopup from "./components/AgreementPopup";

function App() {
  return (
    <>
      <Header />
      <AgreementPopup />
      <Router>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/image" element={<Image />} />
          <Route path="/sentiment" element={<Sentimental />} />
          <Route path="/instagram" element={<Instagram />} />
          <Route path="/report" element={<Report />} />
        </Routes>
      </Router>
      <Footer />
    </>
  );
}

export default App;
