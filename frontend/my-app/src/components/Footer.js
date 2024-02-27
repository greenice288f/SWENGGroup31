import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'; 
import { faXTwitter, faYoutube, faLinkedin, faFacebook, faInstagram } from '@fortawesome/free-brands-svg-icons'; 
import '../components/Footer.css';
{/* npm install @fortawesome/react-fontawesome*/}
{/* npm install @fortawesome/free-brands-svg-icons*/}

export default function Footer(){

    return(
      <> 
        <div className='container'>
          <div className='content'>
            {/* row 1 */}
            <div className='row'>
              <div className='button-group-1'>
                 <a className='linkedin' href="https://www.linkedin.com/company/munich-re/" >
                  <FontAwesomeIcon icon={faLinkedin}/>
                </a>

                <a className='youtube' href="https://www.youtube.com/user/MunichReVideo" >
                  <FontAwesomeIcon icon={faYoutube}/>
                </a>

                <a className='facebook' href="https://www.facebook.com/munichre/" >
                  <FontAwesomeIcon icon={faFacebook}/>
                </a>

                <a className='x' href="https://twitter.com/munichre" >
                  <FontAwesomeIcon icon={faXTwitter}/>
                </a>

              </div>

            </div>

            <hr/> 
            
            {/*row 2 */}
            <div className='row2'>
              <div className='copyright'>
                &copy; {new Date().getFullYear()} Munich Re and/or its affiliates. All Rights Reserved.
              </div>

              <div className='button-group-2'>
                <a type='button' className='Contact' href="https://www.munichre.com/en/general/contact.html">
                  Contact
                </a>
  
                <a type='button' className='Privacy' href="https://www.munichre.com/en/general/privacy.html">
                  Privacy
                </a>
  
                <a type='button' className='Cookies' href="https://www.munichre.com/en/general/privacy.html#CookieSettings">
                  Cookies
                </a>
              </div>

            </div>
          </div>
        </div>
      </>
    )
}