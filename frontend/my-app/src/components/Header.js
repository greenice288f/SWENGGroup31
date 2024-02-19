import React from 'react'
import '../components/Header.css'

export default function Header(){

    return(
      <> 
        <div className='container'>
          <div className='content'>
            {/* row 1 */}
            <div className='row'>
              <div className='button-group-1'>
                <a type='button' className='Placeholder' href="https://example.com">
                  Button placeholder
                </a>
              </div>

            </div>
            <hr/>
          </div>
        </div>
      </>
    )
}