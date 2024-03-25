import React, { useState } from 'react';
import AgreementPopup from "../components/AgreementPopup";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Button from '../components/Button';
import LoadingSpinner from '../components/LoadingSpinner';

function Instagram() {

  const [inputtedText, setInputtedText] = useState();
  const [page, setPage] = useState(0);
  const [newPics, setPics] = useState(<></>);

  const instagramAnalysis = async () => {
    console.log(inputtedText)
    try {
      const origin = window.location.hostname === 'localhost' ? 'https://127.0.0.1:5000' : window.location.origin;
      const response = await fetch(`${origin}/api/instagram-analysis`)

      if (response.ok) {
        const data = await response.json(); // Parse the response data
        console.log('data arived')
        console.log(data)
        const base64images = JSON.parse(data.images);
        const imageDataas = JSON.parse(data.info)
        setPics(
          <div style={{ display: 'flex', flexDirection: 'row', flexWrap: 'wrap' }}>
            <h1>Total Score: {imageDataas[1]}</h1>

            {base64images.map((base64String, index) => {
              // You can write JavaScript code here
              console.log('Rendering image', index);
              let string = ""
              let value = 0
              let len = imageDataas[0][index].length
              if (imageDataas[0][index][len - 2] === 0) {
                string = "no evidence of smoking"
                value = 0
              } else if (imageDataas[0][index][len - 2] === 1) {
                string = "evidence of smoking, cigarette near face"
                value = imageDataas[0][index][0]
              } else if (imageDataas[0][index][len - 2] === 2) {
                string = "evidence of smoking, cigarette near hand"
                value = imageDataas[0][index][0]
              } else {
                string = "evidence of smoking, only cigarette detected"
                value = imageDataas[0][index][0]
              }
              return (
                <div style={{ width: '200px', margin: '10px' }}>
                  <img
                    key={index}
                    src={`data:image/png;base64,${base64String}`}
                    alt={`Image ${index + 1}`}
                    style={{ width: '100%', height: 'auto' }}
                  />
                  <h3>{string} confidence of smoking: {value}</h3>
                </div>
              );
            })}

          </div>
        )
        setPage(1)
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
        <div
          style={{
            marginTop: "30px",
            textAlign: "center",
            width: "100%",
            padding: "120px 0px"
          }}>
          <h1>Click the button to determine smoker status</h1>
          {page === 0 ? (
            <>
              <div>
                <Button onClick={() => { instagramAnalysis(); setPage(2); }}>Analyse</Button>
              </div>
            </>) : page === 1 ? (
              <>
                {newPics}
              </>
            ) : (
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <LoadingSpinner />
            </div>
          )}

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