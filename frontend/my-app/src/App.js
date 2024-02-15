import React, { useState } from 'react';
import Image from './Image';
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";

function App() {

  return (
    <Router>
        <Routes>
            <Route path="/image" element={<Image />} />
        </Routes>
    </Router>
  );
}

export default App;
