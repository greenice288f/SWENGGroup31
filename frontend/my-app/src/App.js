import React from 'react';
import Image from './Image';
import Main from './Main';
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";

function App() {
  return (
    <Router>
        <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/image" element={<Image />} />
        </Routes>
    </Router>
  );
}

export default App;
