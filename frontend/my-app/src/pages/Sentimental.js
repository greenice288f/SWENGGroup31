import React, { useState } from 'react';
import Header from '../components/Header';
import AgreementPopup from '../components/AgreementPopup';



function Sentimental() {
    const [inputtedText, setInputtedText] = useState();
    const [outputText, setOutputText] = useState();
    
    function handleAnalyze() {
        /* TODO: do whatever is needed with this, this is called when analyze is pressed. */
        setOutputText(inputtedText);
    }

    return ( 
    <>
        <Header></Header>
        <AgreementPopup></AgreementPopup>
        <div 
        style={{
        display: 'inline-block', 
        textAlign: "center", 
        width: "100%",
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
        <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            'flex-wrap': 'wrap',
            'padding-top': '20px'
        }}>
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