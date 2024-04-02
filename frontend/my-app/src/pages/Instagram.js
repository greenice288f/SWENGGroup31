import React, { useState } from "react";
import Button from "../components/Button";
import Report from "../pages/Report";
import LoadingSpinner from "../components/LoadingSpinner";

function Instagram() {
  const [loading, setLoading] = useState(false);
  const [reportData, setReportData] = useState(null);
  const [name, setName] = useState("");
  const test = "test";

  const instagramAnalysis = async () => {
    try {
      const origin =
        window.location.port === "3000"
          ? "https://localhost:5000"
          : window.location.origin;

      const response = await fetch(`${origin}/api/instagram-analysis`, {
        mode: "cors",
      });

      if (response.ok) {
        const data = await response.json(); // Parse the response data
        console.log("data arrived");
        console.log(data);
        setReportData(data);
        setLoading(false);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return reportData == null ? (
    <>
      <section class="page-container">
        <div
          style={{
            marginTop: "30px",
            textAlign: "center",
            width: "100%",
            padding: "120px 0px",
          }}
        >
          <h1>Instagram verified successfully!</h1>
          <h2>Please enter your details below to generate report</h2>
          {!loading ? (
            <>
              <div>
                <form style={{ padding: "1%" }}>
                  <label>
                    {"Enter your full name:\t"}
                    <input
                      style={{ fontSize: "14px" }}
                      type="text"
                      onInput={(e) => setName(e.target.value)}
                    />
                  </label>
                </form>
                <Button
                  onClick={() => {
                    if (name != "") {
                      setLoading(true);
                      instagramAnalysis();
                    }
                  }}
                >
                  Analyse
                </Button>
              </div>
            </>
          ) : (
            <div
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                marginTop: "5%",
              }}
            >
              <LoadingSpinner />
            </div>
          )}
        </div>
      </section>
    </>
  ) : (
    <Report smoker_report={reportData} report_name={name} />
  );
}

export default Instagram;
