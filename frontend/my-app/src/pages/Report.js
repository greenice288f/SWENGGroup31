import { useState } from "react";
import Header from "../components/Header";
import ScoreBar from "../components/ScoreBar";
import "./pages.css";

function Report() {
  const [name, setName] = useState("James Gray");
  const [username, setUsername] = useState("undefined");
  const [images, setImages] = useState([]);
  const [score, setScore] = useState(10.0);
  const [date, setDate] = useState("1/1/0000");

  return (
    <>
      <Header />
      <div class="title-container">
        <div class="title-card">
          <h1>Report for {name}</h1>
          <h3>Instagram: @{username}</h3>
          <h3>Generated on {date}</h3>
        </div>
        <div class="title-card">
          <ScoreBar score={score} />
          <div style={{ "padding-left": "10px" }}>
            Smoker risk score: {score}
          </div>
        </div>
      </div>
    </>
  );
}

export default Report;
