import { useState } from "react";
import Header from "../components/Header";
import ScoreBar from "../components/ScoreBar";
import "./report.css";

function Report() {
  const img_src = require("../components/CigarMan.png");

  const [name, setName] = useState("James Gray");
  const [username, setUsername] = useState("undefined");
  const [images, setImages] = useState(Array(3).fill(img_src));
  const [score, setScore] = useState(10.0);
  const [date, setDate] = useState("1/1/0000");

  return (
    <>
      <Header />
      <div class="report">
        <div class="title-container">
          <div class="title-cards">
            <div class="card">
              <h1>Report for {name}</h1>
              <h3>Instagram: @{username}</h3>
              <h3>Generated on {date}</h3>
            </div>
            <div class="card">
              <ScoreBar score={score} />
              <h3 style={{ "padding-left": "8px" }}>
                Smoker risk score: {score}
              </h3>
            </div>
          </div>
          <h2 style={{ "text-align": "center" }}>
            Based on this Instagram account's score, they are likely a smoker!
          </h2>
        </div>
        <div class="image-container">
          <div class="image-cards">
            {images.map((image) => (
              <div class="card">
                <img src={img_src} alt="" style={{ width: "50%" }} />
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

export default Report;
