import './App.css';
import { useState } from 'react';

function App() {
  const [uploadedImage, setUploadedImage] = useState();

  return (
    <div>
      <h1>Upload an image to test cigarette detection</h1>

      {uploadedImage && (
        <div>
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
      <br />
      
      <input
        type="file"
        name="myImage"
        onChange={(event) => {
          console.log(event.target.files[0]);
          setUploadedImage(event.target.files[0]);
        }}
      />
    </div>
  );
}

export default App;
