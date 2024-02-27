import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import AgreementPopup from '../components/AgreementPopup';
import '../components/stylez.css';

function Sentimental() {
    const [inputtedText, setInputtedText] = useState();
    const [outputText, setOutputText] = useState();

    function handleAnalyze() {
        /* TODO: do whatever is needed with this, this is called when analyze is pressed. */
        setOutputText(inputtedText);
    }

    return (
        <>
            <Header />
            <AgreementPopup />
            <div
                style={{
                    display: 'inline-block',
                    textAlign: "center",
                    width: "100%",
                }}>
                <div class='about-col'>
                    <h1>Sentiment Analysis</h1>
                </div>
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
            {/* temp links */}
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                'flex-wrap': 'wrap',
                'padding-top': '20px'
            }} />
            <Footer />
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