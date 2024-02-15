import React, { useState } from 'react';
import { Link } from "react-router-dom";

function Image () {
    
    const [uploadedImage, setUploadedImage] = useState();

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
        try{
          const base64Image = await convertImageToBase64(uploadedImage);
          console.log('Base64 image:', base64Image);
          const image = { 
            lmao: base64Image
           };
          const response = await fetch("http://127.0.0.1:5000/upload", {
          method: "POST",
          headers: {
          'Content-Type' : 'application/json',
          },
          body: JSON.stringify(image)
          })
          if (response.ok) {
            const data = await response.json(); // Parse the response data
            console.log(data)
          }
        }catch (error) {
          console.error('Error fetching data:', error);
        }
      };

    return (
        <div>
            <h1 style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
            }}>
            Upload an image to test cigarette detection
            </h1>
    
            {uploadedImage && (
                <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                'flex-wrap': 'wrap'
                }}>
                <img
                    alt="not found"
                    width={"800px"}
                    src={URL.createObjectURL(uploadedImage)}
                />
                <div style={{ 'flex-basis': '100%', height: '20px' }} />
                <button
                    onClick={() => setUploadedImage(null)}
                >
                    Remove
                </button>
                </div>
            )}
            <br />
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
            }}>
                <input
                type="file"
                name="myImage"
                onChange={(event) => {
                    console.log(event.target.files[0]);
                    setUploadedImage(event.target.files[0]);
                }}
                />
                <button onClick={handleUpload}>Upload</button>
            </div>
            <div>
              <ul>
                  <li>
                      <Link to="/">Home</Link></li>
                  <li>
                      <Link to="/sentimental">Sentimental Analysis</Link>
                  </li>
                  <li>
                      <Link to="/image">Image Analysis</Link>
                  </li>
              </ul>
            </div>
        </div>
    );
}

export default Image;