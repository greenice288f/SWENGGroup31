import React from "react";
import "../components/Header.css";
import "../components/stylez.css";
import logo from "./logo.png";

function Header() {
  const origin =
    window.location.hostname === "localhost"
      ? "https://localhost:5000"
      : window.location.origin;
  const redirectUri = encodeURIComponent(`${origin}/api/instagram-redirect`);
  const instagramUrl = `https://api.instagram.com/oauth/authorize?client_id=427613722975596&redirect_uri=${redirectUri}&scope=user_profile,user_media&response_type=code`;

  return (
    <>
      <section className="sub-header">
        <nav>
          <a href="/">
            <img src={logo} alt="Munich Re logo" />
          </a>
          <div className="navlinks">
            <ul>
              <li>
                <a type="button" className="headerlink" href="/">
                  Main
                </a>
              </li>
              <li>
                <a type="button" className="headerlink" href="/sentiment">
                  Sentiment Analysis
                </a>
              </li>
              <li>
                <a type="button" className="headerlink" href="/image">
                  Image Analysis
                </a>
              </li>
              <li>
                <a type="button" className="headerlink" href={instagramUrl}>
                  Instagram Analysis
                </a>
              </li>
              <li>
                <a type="button" className="headerlink" href="/faq">
                  FAQ
                </a>
              </li>
            </ul>
          </div>
        </nav>
      </section>
    </>
  );
}

export default Header;
