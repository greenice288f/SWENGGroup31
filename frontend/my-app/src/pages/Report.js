import { useState } from "react";
import ScoreBar from "../components/ScoreBar";
import ScoreRing from "../components/ScoreRing";
import "./report.css";

function Report() {
  const img_src = require("../components/CigarMan.png");

  const [name, setName] = useState("James Gray");
  const [username, setUsername] = useState("undefined");
  const [images, setImages] = useState(Array(3).fill(img_src));
  const [score, setScore] = useState(70);
  const [date, setDate] = useState("1/1/0000");

  let scoreDescription =
    score > 60
      ? "Based on this Instagram account's score, they are likely a smoker!"
      : score > 20
        ? "Based on this Instagram account's score, they may be a smoker!"
        : "Based on this Instagram account's score, they are unlikely to be a smoker!";

  return (
    <>
      <div class="report page-container">
        <div class="title-container">
          <div class="title-cards">
            <div class="card" style={{ "margin-right": "1%" }}>
              <h1>Report for {name}</h1>
              <h3>Instagram: @{username}</h3>
              <h3>Generated on {date}</h3>
            </div>
            <div class="card" style={{ "margin-left": "1%" }}>
              <ScoreBar score={score} />
              <h3 style={{ "padding-left": "8px" }}>
                Smoker risk score: {score}
              </h3>
            </div>
          </div>
          <h2 style={{ "text-align": "center" }}>{scoreDescription}</h2>
        </div>
        <div class="image-container">
          <div class="image-cards">
            {images.map((image) => (
              <div class="card image-card">
                <img src={image} alt="" style={{ width: "50%" }} />
                <div class="image-desc">
                  <ScoreRing score={score} />
                  <h4>Notes:</h4>
                  <div>
                    Three cigarettes detected. Cigarette detected near face...
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

export default Report;
