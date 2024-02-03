import logo from './logo.svg';
import './App.css';
import React from 'react';

function App() {
  const [message, setMessage]=React.useState("")


  function buttonPressed(){
    fetch('http://127.0.0.1:5000/sokaigeljenorbitron')
    .then(response => {
      if (!response.ok) {
        throw new Error('No response received');
      }
      return response.json();
    })
    .then(data => {
      setMessage(data.message)
      console.log(data.message)
    })
    .catch(error => {
      setMessage("u forgot to start the server u stooopid")
      // Show an error message to the user
    });

  }
  return (
    <div className="App">
    <button onClick={buttonPressed}>Press me</button>
    <p>{message}</p>
    </div>
  );
}

export default App;
