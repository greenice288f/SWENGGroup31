import React from 'react';
import Image from './pages/Image';
import Sentimental from './pages/Sentimental';
import Main from './pages/Main';

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
            <Route path="/sentimental" element={<Sentimental />} />
        </Routes>
    </Router>
  );
}

export default App;
