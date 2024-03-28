import React, { useState } from "react";
import Team from "../components/Team";
import "./pages.css";
import "./faq.css";
const Faq = () => {
  const [answersVisible, setAnswersVisible] = useState({});
  const origin =
  window.location.hostname === "localhost"
    ? "https://localhost:5000"
    : window.location.origin;
  // Function to toggle answer visibility
  const toggleAnswer = (category, index) => {
    setAnswersVisible((prevAnswersVisible) => {
      const key = `${category}-${index}`;
      return { ...prevAnswersVisible, [key]: !prevAnswersVisible[key] };
    });
  };

  return (
   <body>
      <section id="faq">
        <br></br>
  <div className="faq-container">
   

    <div className="wrapper">
      {/* FAQ groups */}
      <div className="faq-group">
        <h1 className="faq-group-title">General Questions</h1>
        <ul className="faq-list">
          <li className="faq-item">
            <button
              className="faq-question"
              onClick={() => toggleAnswer("general", 1)}
            >
              What is Lorem Ipsum?
            </button>
            {answersVisible["general-1"] && (
              <p className="faq-answer">
                Lorem Ipsum is simply dummy text of the printing and
                typesetting industry.
              </p>
            )}
          </li>
          <li className="faq-item">
            <button
              className="faq-question"
              onClick={() => toggleAnswer("general", 2)}
            >
              Why do we use it?
            </button>
            {answersVisible["general-2"] && (
              <p className="faq-answer">
                It is a long established fact that a reader will be
                distracted by the readable content of a page when looking
                at its layout.
              </p>
            )}
          </li>
      
        </ul>
      </div>
    </div>
  </div>
</section>
<Team />
</body>
  
    
  );
};

export default Faq;
