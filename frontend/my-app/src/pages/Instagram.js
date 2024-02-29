import React, { useState } from 'react';
import AgreementPopup from "../components/AgreementPopup";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Button from '../components/Button';

function Instagram() {

    const [inputtedText, setInputtedText] = useState();
    const handleUpload =
    async () => {
        console.log(inputtedText)
      try {
        const image = {
            username: "xd"
        };
        const response = await fetch("http://127.0.0.1:5000/user", {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(image)
        })
        if (response.ok) {
          const data = await response.json(); // Parse the response data
          console.log('done')
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    return (
        <>
            <Header />
            <AgreementPopup />
            <section>
                <div class='about-col'
                    style={{
                        display: 'inline-block',
                        textAlign: "center",
                        width: "100%",
                    }}>
                    <h1>Enter an instagram username to determine smoker status</h1>
                    <div>
                        <InputForm inputFunction={setInputtedText} />
                    </div>
                    <div>
                        <Button onClick={() => {handleUpload(); }}>Enter</Button>
                    </div>
                </div>
            </section>
            <Footer />
        </>
    );
}

function InputForm({ inputFunction }) {
    return (
        <form>
            <textarea name="text" style={{ resize: 'none', width: "60%", height: "2vh", margin: '20px', padding: '20px' }} onChange={e => inputFunction(e.target.value)} />
        </form>
    );
}

export default Instagram;