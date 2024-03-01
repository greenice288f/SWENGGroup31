import React, { useState } from 'react';
import AgreementPopup from "../components/AgreementPopup";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Button from '../components/Button';
import LoadingSpinner from '../components/LoadingSpinner';

function Instagram() {

    const [inputtedText, setInputtedText] = useState();
    const [page, setPage]=useState(0);
    const [newPics, setPics] = useState(<></>);

    const handleUpload =
    async () => {
        console.log(inputtedText)
      try {
        const image = {
            username: "xd"
        };
        const response = await fetch(`${window.location.origin}/api/user`, {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(image)
        })
        if (response.ok) {
          const data = await response.json(); // Parse the response data
          console.log('data arived')
          console.log(data)
          const myArray = JSON.parse(data.images);
          setPics(
          <div>
            {myArray.map((base64String, index) => (
              <img
                key={index}
                src={`data:image/png;base64,${base64String}`}
                alt={`Image ${index + 1}`}
              />
            ))}
          </div>
          )
          console.log(myArray.length)
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
                <div class='about-col'
                    style={{
                        display: 'inline-block',
                        textAlign: "center",
                        width: "100%",
                    }}>
                    <h1>Enter an instagram username to determine smoker status</h1>
                    {page ===0?(
                    <>
                        <div>
                        <InputForm inputFunction={setInputtedText} />
                        </div>
                        <div>
                            <Button onClick={() => {handleUpload(); setPage(2);}}>Enter</Button>
                        </div>
                    </>): page === 1 ? (
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