import "./ScoreBar.css";

function ScoreBar({ score }) {
  const score_percent = score + "%";
  const score_colour = score < 30 ? "red" : score < 60 ? "orange" : "green";
  return (
    <>
      <div class="score-bar">
        <span
          style={{ width: score_percent, "background-color": score_colour }}
        />
      </div>
    </>
  );
}

export default ScoreBar;
