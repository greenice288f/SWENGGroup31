import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
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
            <div
                class="page-container" 
                style={{
                    display: 'inline-block',
                    textAlign: "center",
                    width: "100%",
                }}>
                <h1>Sentiment Analysis</h1>
                <InputForm inputFunction={setInputtedText} />
                <div>
                    <button size='xl' onClick={handleAnalyze}>
                        Analyze
                    </button>
                </div>
                <div>
                    {outputText}
                </div>
            </div>
        </>
    );
}

function InputForm({ inputFunction }) {
    return (
        <form>
            <textarea name="text" style={{ resize: 'none', width: "60%", height: "70vh", margin: '15px', padding: '15px' }} onChange={e => inputFunction(e.target.value)} />
        </form>
    );
}

export default Sentimental;