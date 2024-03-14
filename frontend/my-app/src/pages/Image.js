import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import LoadingSpinner from '../components/LoadingSpinner';
import AgreementPopup from '../components/AgreementPopup';
import Button from '../components/Button';

function Image() {
  const [uploadedImage, setUploadedImage] = useState();
  const [newPics, setPics] = useState("");
  //0 upload, 1 result, 2 loading
  const [imageWindow, setImageWindow] = useState(0)


  function convertImageToBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        const base64String = reader.result.split(',')[1]; // Extract the Base64 part
        resolve(base64String);
      };
      reader.onerror = (error) => {
        reject(error);
      };
    });
  }
  const handleUpload =

    async () => {
      try {
        const base64Image = await convertImageToBase64(uploadedImage);
        const image = {
          lmao: base64Image
        };
        const origin = window.location.hostname === 'localhost' ? 'http://127.0.0.1:5000' : window.location.origin;
        const response = await fetch(`${origin}/api/upload`, {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(image)
        })
        if (response.ok) {
          const data = await response.json(); // Parse the response data

          //const binaryData = base64ToBinary(data.image);
          setPics(data.image);
          console.log(data.data);
          const newString = JSON.stringify(data.data.predictions);
          const res = (newString.length > 2) ? "Evidence of smoking detected!" : "No evidence of smoking found...";
          setPics(
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', 'flex-direction': 'column' }}>
              {uploadedImage && (
                <div>
                  <img alt="not found" width="500px" src={`data:image/png;base64,` + data.image} />
                </div>
              )}
              <div>{res}</div>
            </div>
          );
          setImageWindow(1);
          console.log('done')
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };


  return (
    <>
      <Header></Header>
      <AgreementPopup></AgreementPopup>
      <div>
        <div style={{
          display: 'inline-block',
          textAlign: "center",
          width: "100%",
        }}>
          <div class='about-col'>
            <h1>Upload an image to test cigarette detection</h1>
          </div>
        </div>

        {imageWindow === 0 ? (
          <>
            {uploadedImage && (
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexWrap: 'wrap' }}>
                <img alt="not found" width="500px" src={URL.createObjectURL(uploadedImage)} />
              </div>
            )}
          </>
        ) : imageWindow === 1 ? (
          <>
            {newPics}
          </>
        ) : (
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <LoadingSpinner />
          </div>
        )}


        <br />
      </div>
      <section class="about-us">
        <div class="row">
          <div class="about-col">
            <input
              type="file"
              name="myImage"
              class="addFile"
              onChange={(event) => {
                setImageWindow(0);
                console.log(event.target.files[0]);
                setUploadedImage(event.target.files[0]);
              }}
            />
            <div style={{'display': 'flex', 'justify-content': 'center', paddingBottom: "70px"}}>
              <Button theme='red' onClick={() => { setUploadedImage(null); setImageWindow(0); }}>Remove</Button>
              <Button onClick={() => { setImageWindow(2); handleUpload(); }}>Upload</Button>
            </div>
          </div>
        </div>
      </section>
      <Footer />
    </>
  );
}

export default Image;
