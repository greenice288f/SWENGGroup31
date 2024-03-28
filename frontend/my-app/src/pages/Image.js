import React, { useState } from "react";
import LoadingSpinner from "../components/LoadingSpinner";
import Button from "../components/Button";
import convertImageToBase64 from "../tools/ImageTools";

const PAGE_TITLE = "Log-in below to generate a report";

function Image() {
  const [uploadedImage, setUploadedImage] = useState();
  const [newPics, setPics] = useState("");
  const [imageWindow, setImageWindow] = useState(0);

  const handleUpload = async () => {
    try {
      const base64Image = await convertImageToBase64(uploadedImage);
      const image = {
        lmao: base64Image,
      };
      const origin =
        window.location.hostname === "localhost"
          ? "https://127.0.0.1:5000"
          : window.location.origin;
      const response = await fetch(`${origin}/api/upload`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(image),
      });
      if (response.ok) {
        const data = await response.json(); // Parse the response data

        //const binaryData = base64ToBinary(data.image);
        setPics(data.image);
        console.log(data.data);
        const newString = JSON.stringify(data.data.predictions);
        const res =
          newString.length > 2
            ? "Evidence of smoking detected!"
            : "No evidence of smoking found...";
        setPics(
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              "flex-direction": "column",
            }}
          >
            {uploadedImage && (
              <div>
                <img
                  alt="not found"
                  width="500px"
                  src={`data:image/png;base64,` + data.image}
                />
              </div>
            )}
            <div>{res}</div>
          </div>,
        );
        setImageWindow(1);
        console.log("done");
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div class="page-container">
      <div>
        <div
          style={{
            display: "inline-block",
            textAlign: "center",
            width: "100%",
          }}
        >
          <div class="about-col">
            <h1>{PAGE_TITLE}</h1>
          </div>
        </div>

        {imageWindow === 0 ? (
          <>
            {uploadedImage && (
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  flexWrap: "wrap",
                }}
              >
                <img
                  alt="not found"
                  width="500px"
                  src={URL.createObjectURL(uploadedImage)}
                />
              </div>
            )}
          </>
        ) : imageWindow === 1 ? (
          <>{newPics}</>
        ) : (
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
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
            <div
              style={{
                display: "flex",
                "justify-content": "center"
              }}
            >
              <Button
                theme="red"
                onClick={() => {
                  setUploadedImage(null);
                  setImageWindow(0);
                }}
              >
                Remove
              </Button>
              <Button
                onClick={() => {
                  setImageWindow(2);
                  handleUpload();
                }}
              >
                Upload
              </Button>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Image;
