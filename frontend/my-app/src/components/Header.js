import React from 'react';
import '../components/Header.css';
import '../components/stylez.css';
import logo from './logo.png';


function Header() {
  return (
    <>
   
      <section className="sub-header">
        <nav>
          <a href="/"><img src={logo} alt="Munich Re logo" /></a>
          <div className="navlinks">
            <ul>
              <li><a type='button' className='headerlink' href="/">Main</a></li>
              <li><a type='button' className='headerlink' href="/sentiment">Sentiment Analysis</a></li>
              <li><a type='button' className='headerlink' href="/image">Image Analysis</a></li>
              <li><a type='button' className='headerlink' href="/instagram">Instagram Analysis</a></li>
            </ul>
          </div>
        </nav>
      </section>
    </>
  );
}

export default Header;
