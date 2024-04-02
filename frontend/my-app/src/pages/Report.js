import { useState } from "react";
import ScoreBar from "../components/ScoreBar";
import ScoreRing from "../components/ScoreRing";
import "./report.css";

function Report(props) {
  const smoker_report = props.smoker_report;
  const name = props.report_name;

  const [username, setUsername] = useState("undefined");
  const [images, setImages] = useState(JSON.parse(smoker_report.images));
  const date = new Date().toLocaleDateString();

  const base64images = JSON.parse(smoker_report.images);
  const imageDescriptions = JSON.parse(smoker_report.info);

  let descriptions = [];
  let certainties = [];
  let sum = 0;
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
    sum += descriptiveValue;
  }
  const imageScore = (sum * 100) / certainties.length;

  const sentimentList = JSON.parse(smoker_report.info)[3];
  let commentList = [];
  let sentScoresList = [];
  for (let i = 0; i < sentimentList.length; i++) {
    commentList.push(sentimentList[i][0]);
    sentScoresList.push(sentimentList[i][1]);
  }

  const sentimentScore = 100 * JSON.parse(smoker_report.info)[2];
  const overallScore = Math.round(0.7 * imageScore + 0.3 * sentimentScore);
  let scoreDescription =
    overallScore > 60
      ? "Based on this Instagram user's score, they are likely a smoker!"
      : overallScore > 20
        ? "Based on this Instagram user's score, they may be a smoker!"
        : "Based on this Instagram user's score, they are unlikely to be a smoker!";

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
              <ScoreBar score={overallScore} />
              <h3 style={{ "padding-left": "8px" }}>
                Smoker risk score: {overallScore}%
              </h3>
            </div>
          </div>
          <h2 style={{ "text-align": "center" }}>{scoreDescription}</h2>
        </div>
        <div class="image-container">
          <div class="image-cards">
            <h1 style={{ paddingLeft: "10%" }}>Posts:</h1>
            {images.map((base64String, index) => (
              <div class="card image-card">
                <img
                  key={index}
                  src={`data:image/png;base64,${base64String}`}
                  alt=""
                  style={{ width: "50%" }}
                />
                <div class="image-desc">
                  <ScoreRing score={Math.round(certainties[index] * 100)} />
                  <h4>Notes:</h4>
                  <div>{descriptions[index]}</div>
                </div>
              </div>
            ))}
          </div>
          <div class="image-cards">
            <h1 style={{ paddingLeft: "10%" }}>Comments:</h1>
            {commentList.map((comment, index) => (
              <div class="card comment-card">
                <div class="image-desc">
                  <ScoreRing score={Math.round(sentScoresList[index] * 100)} />
                  <h4>Comment:</h4>
                  <div>{comment}</div>
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
