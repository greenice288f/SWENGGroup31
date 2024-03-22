import { React, useState } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import Button from "../components/Button";
import AgreementPopup from "../components/AgreementPopup";
import "./pages.css";

function Main() {
  const origin =
    window.location.hostname === "localhost"
      ? "https://localhost:5000"
      : window.location.origin;
  const redirectUri = encodeURIComponent(`${origin}/api/instagram-redirect`);
  const instagramUrl = `https://api.instagram.com/oauth/authorize?client_id=427613722975596&redirect_uri=${redirectUri}&scope=user_profile,user_media&response_type=code`;

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
            margin: "2%",
          }}
        >
          <h2>Welcome!</h2>
          <h2>Log-in to your instagram below to generate a report.</h2>
          <div style={{ margin: "2%" }}>
            <Button as="a" href={instagramUrl}>
              LOGIN TO INSTAGRAM
            </Button>
          </div>
        </div>
      </body>
      <Footer />
    </div>
  );
}

export default Main;
