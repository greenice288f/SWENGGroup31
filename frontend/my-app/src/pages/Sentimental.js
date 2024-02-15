import React, { useState } from 'react';

function Sentimental() {
    const [inputtedText, setInputtedText] = useState();
    
    return ( <>
    <div style={{display: 'inline-block', textAlign: "center", width: "100%"}}>
        <label>Sentimental Analysis</label>
        <InputForm inputFunction={setInputtedText}/>
        <button>Submit</button> 
        <br/><label>{inputtedText}</label>
    </div>
    
    </>
    );
}

function InputForm({inputFunction}) {
    return ( 
        <form>
            <textarea name="text" style={{width: "80%", height: "80vh" }} onChange={e => inputFunction(e.target.value)}/>
        </form>
    );
}

export default Sentimental;