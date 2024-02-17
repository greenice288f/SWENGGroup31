import React, { useState } from 'react';
import { Link } from "react-router-dom";

function Sentimental() {
    const [inputtedText, setInputtedText] = useState();
    const [outputText, setOutputText] = useState();
    
    function handleAnalyze() {
        /* TODO: do whatever is needed with this, this is called when analyze is pressed. */
        setOutputText(inputtedText);
    }

    return ( 
    <>
        <div 
        style={{
        display: 'inline-block', 
        textAlign: "center", 
        width: "100%"
        }}>
            <h1>
                Sentimental Analysis
            </h1>
            <InputForm inputFunction={setInputtedText}/>
            <button onClick={handleAnalyze}>
                Analyze
            </button> 
            <div>
                {outputText}
            </div>
        </div>
        {/* temp links */}
        <div>
            <ul>
                  <li>
                      <Link to="/">Home</Link>
                  </li>
                  <li>
                      <Link to="/sentimental">Sentimental Analysis</Link>
                  </li>
                  <li>
                      <Link to="/image">Image Analysis</Link>
                  </li>
            </ul>
        </div>
    </>
    );
}

function InputForm({inputFunction}) {
    return ( 
        <form>
            <textarea name="text" style={{width: "80%", height: "70vh" }} onChange={e => inputFunction(e.target.value)}/>
        </form>
    );
}

export default Sentimental;