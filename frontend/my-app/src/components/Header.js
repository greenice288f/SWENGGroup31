import React from 'react';
import '../components/Header.css';
import '../components/stylez.css';
import logo from './CigarMan.png';


function Header() {
  return (
    <>
   
      <section className="sub-header">
        <nav>
          <a href="alt.html"><img src={logo} alt="Cigar Man3" /></a>
          <div className="navlinks">
            <ul>
              <li><a type='button' className='headerlink' href="/">Main</a></li>
              <li><a type='button' className='headerlink' href="/sentimental">Sentimental Analysis</a></li>
              <li><a type='button' className='headerlink' href="/image">Image Analysis</a></li>
            
            </ul>
          </div>
        </nav>
      </section>
    </>
  );
}

export default Header;
