import React, { useState } from 'react';

function App() {
  const [uploadedImage, setUploadedImage] = useState();
  const [newPics, setPics] = useState("");
  const [togglePics, setToggle]= useState(true)


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
      
        //const binaryData = base64ToBinary(data.image);
        setPics(data.image)
        setToggle(false)
        //createImageFromBinary(binaryData);
        console.log('done')
        
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
      {togglePics ? <>{uploadedImage && (
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
        </div>
      )}</> :
       <>
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
            src={"data:image/png;base64," + newPics}
          />
        </div>
      )}
       </>}
       <div style={{ 'flex-basis': '100%', height: '20px' }} />
      <br />
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
      }}>
      <button onClick={() => { setUploadedImage(null); setToggle(true); }}>Remove</button>

        <input
          type="file"
          name="myImage"
          onChange={(event) => {
            setToggle(true)
            console.log(event.target.files[0]);
            setUploadedImage(event.target.files[0]);
          }}
        />
        <button onClick={handleUpload}>Upload</button>
      </div>
    </div>
  );
}

export default App;
