import { useState } from "react";
import ScoreBar from "../components/ScoreBar";
import ScoreRing from "../components/ScoreRing";
import "./report.css";

function Report({ smoker_report }) {
  const img_src = require("../components/CigarMan.png");

  const [name, setName] = useState("James Gray");
  const [username, setUsername] = useState("undefined");
  const [images, setImages] = useState(JSON.parse(smoker_report.images));
  const [score, setScore] = useState(70);
  const [date, setDate] = useState("1/1/0000");

  const base64images = JSON.parse(smoker_report.images);
  const imageDescriptions = JSON.parse(smoker_report.info);

  let scoreDescription =
    score > 60
      ? "Based on this Instagram account's score, they are likely a smoker!"
      : score > 20
        ? "Based on this Instagram account's score, they may be a smoker!"
        : "Based on this Instagram account's score, they are unlikely to be a smoker!";

  let descriptions = [];
  let certainties = [];
  for (let i = 0; i < base64images.length; i++) {
    let description = "";
    let descriptiveValue = 0;
    let len = imageDescriptions[0][i].length;
    if (imageDescriptions[0][i][len - 2] === 0) {
      description = "no evidence of smoking";
      descriptiveValue = 0;
    } else if (imageDescriptions[0][i][len - 2] === 1) {
      description = "evidence of smoking, cigarette near face";
      descriptiveValue = imageDescriptions[0][i][0];
    } else if (imageDescriptions[0][i][len - 2] === 2) {
      description = "evidence of smoking, cigarette near hand";
      descriptiveValue = imageDescriptions[0][i][0];
    } else {
      description = "evidence of smoking, only cigarette detected";
      descriptiveValue = imageDescriptions[0][i][0];
    }
    descriptions.push(description);
    certainties.push(descriptiveValue);
  }

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
            {images.map((base64String, index) => (
              <div class="card image-card">
                <img
                  key={index}
                  src={`data:image/png;base64,${base64String}`}
                  alt=""
                  style={{ width: "50%" }}
                />
                <div class="image-desc">
                  <ScoreRing score={certainties[index] * 100} />
                  <h4>Notes:</h4>
                  <div>{descriptions[index]}</div>
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
