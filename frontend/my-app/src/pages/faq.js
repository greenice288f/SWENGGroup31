import React, { useState } from "react";
import Team from "../components/Team";
import "./pages.css";
import "./faq.css";
const Faq = () => {
  const [answersVisible, setAnswersVisible] = useState({});

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
              {answersVisible["general-1"] ? '- ' : '+ '}
              Who are you?
            </button>
            {answersVisible["general-1"] && (
              <p className="faq-answer">
                We are Group 31 of the 2024 SwEng Industry Projects from Trinity College
                Dublin. We've partnered with Munich RE to provide a product that tackles 
                the struggle of risk assessment in the insurance industry in relation to 
                smoking.
              </p>
            )}
          </li>
          <li className="faq-item">
            <button
              className="faq-question"
              onClick={() => toggleAnswer("general", 2)}
            >
              {answersVisible["general-2"] ? '- ' : '+ '}
              Why?
            </button>
            {answersVisible["general-2"] && (
              <p className="faq-answer">
                It is a well-researched fact that individuals who smoke are at a much higher
                risk of dying or disease than individuals who don't. The purpose of our projects
                is to provide a solution to those who are dishonest in the application process
                using cutting-edge technology, as well as provide the ability to prove and
                reward honesty, in the form of insurance premiums.
              </p>
            )}
          </li>
          <li className="faq-item">
            <button
              className="faq-question"
              onClick={() => toggleAnswer("general", 3)}
            >
              {answersVisible["general-3"] ? '- ' : '+ '}
              How do I use this?
            </button>
            {answersVisible["general-3"] && (
              <p className="faq-answer">
                Simply press the "LOGIN TO INSTAGRAM" button on the main page of the application,
                where you'll be brought to Instagram to share information with the program. Once
                you're connected, you'll be redirected to our analysis page where our A.I. system
                will parse your social media in search of evidence of smoking, through both images
                and text.
              </p>
            )}
          </li>
          <li className="faq-item">
            <button
              className="faq-question"
              onClick={() => toggleAnswer("general", 4)}
            >
              {answersVisible["general-4"] ? '- ' : '+ '}
              Are the results reliable?
            </button>
            {answersVisible["general-4"] && (
              <p className="faq-answer">
                A returned score is provided determining how risky we see the individual as in terms of
                smoking. While we have confidence in the ability of the analysis, this score should be
                used in assistance with a background check and should not be seen as 100% accurate proof
                of smoking.
              </p>
            )}
          </li>
          <li className="faq-item">
            <button
              className="faq-question"
              onClick={() => toggleAnswer("general", 5)}
            >
              {answersVisible["general-5"] ? '- ' : '+ '}
              How do you store my information?
            </button>
            {answersVisible["general-5"] && (
              <p className="faq-answer">
                Downloaded images and/or text stays on our server for a very short time for the purpose of
                processing, but is deleted thereafter. The program does not store and keep any personal information.
                By using the program, you agree to this processing, as well as the 
                Munich RE <a href="https://www.munichre.com/en/general/privacy.html">Privacy Policy</a>.
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
