import { React, useState } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import Button from "../components/Button";
import AgreementPopup from "../components/AgreementPopup";
import "./pages.css";
import "./additional.css";
function Main() {
  const origin =
    window.location.hostname === "localhost"
      ? "https://localhost:5000"
      : window.location.origin;
  const redirectUri = encodeURIComponent(`${origin}/api/instagram-redirect`);
  const instagramUrl = `https://api.instagram.com/oauth/authorize?client_id=427613722975596&redirect_uri=${redirectUri}&scope=user_profile,user_media&response_type=code`;

  return (
    <div class="page-container">
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
           <section id="template">
      <div className="template-container">
        <div className="content">
          <div className="flex">
            <span className="topper">How to use the App</span>
           
          </div>
          <ul className="ul">
            <li className="li">
              <span className="number">01</span>
              <p className="li-text">
                Log into your Instagram Account...
              </p>
            </li>
            <li className="li">
              <span className="number">02</span>
              <p className="li-text">
                Let our App determine your smoker status using cutting-edge technology
              </p>
            </li>
            <li className="li">
              <span className="number">03</span>
              <p className="li-text">
                Receive your smoker score and download the results in a handy PDF
              </p>
            </li>
          </ul>
        </div>
      </div>
    
    </section>
      </body>
    </div>
  );
}

export default Main;
