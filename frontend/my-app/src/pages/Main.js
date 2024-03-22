import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import AgreementPopup from "../components/AgreementPopup";
import "./pages.css";

function Main() {
  return (
    <div class="page-container">
      <Header />
      <AgreementPopup />
      <body>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <h2>Welcome!</h2>
          <h2>Log-in to your instagram below to generate a report.</h2>
        </div>
      </body>
      <Footer />
    </div>
  );
}

export default Main;
