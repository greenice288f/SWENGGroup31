import "./ScoreRing.css";

function ScoreRing({ score }) {
  let adjustedScore = score < 90 ? (score > 10 ? score : 10) : 90;
  let ringColour = score > 60 ? "red" : score > 20 ? "orange" : "green";
  const dashOffset = 365 - adjustedScore * 0.01 * 255;
  return (
    <div class="ring-container">
      <svg>
        <circle class="bg" cx="50%" cy="50%" r="25%" />
        <circle
          class="meter"
          cx="50%"
          cy="50%"
          r="25%"
          style={{ "stroke-dashoffset": dashOffset, stroke: ringColour }}
        />
      </svg>
      <h1>{score}%</h1>
    </div>
  );
}

export default ScoreRing;
