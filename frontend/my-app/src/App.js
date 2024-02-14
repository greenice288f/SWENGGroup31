import './App.css';
import { useState } from 'react';

function App() {
  const [uploadedImage, setUploadedImage] = useState();

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
          justifyContent: 'center'
        }}>
          <img
            alt="not found"
            width={"250px"}
            src={URL.createObjectURL(uploadedImage)}
          />
          <br />
          <button onClick={() => setUploadedImage(null)}>Remove</button>
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
      </div>
    </div>
  );
}

export default App;
