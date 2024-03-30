import React, { useState } from "react";
import Button from "../components/Button";
import Report from "../pages/Report";
import LoadingSpinner from "../components/LoadingSpinner";

function Instagram() {
  const [page, setPage] = useState(0);
  const [newPics, setPics] = useState(<></>);
  const [reportData, setReportData] = useState(null);

  const instagramAnalysis = async () => {
    try {
      // const origin =
      //   window.location.hostname === "localhost"
      //     ? "https://127.0.0.1:5000"
      //     : window.location.origin;
      const response = await fetch(
        "https://localhost:5000/api/instagram-analysis",
        {
          mode: "cors",
        },
      );

      if (response.ok) {
        const data = await response.json(); // Parse the response data
        console.log("data arrived");
        console.log(data);
        setReportData(data);
        setPage(1);
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
          <h1>Click the button to determine smoker status</h1>
          {page === 0 ? (
            <>
              <div>
                <Button
                  onClick={() => {
                    instagramAnalysis();
                    setPage(2);
                  }}
                >
                  Analyse
                </Button>
              </div>
            </>
          ) : page === 1 ? (
            <>{newPics}</>
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
    <Report smoker_report={reportData} />
  );
}

export default Instagram;
