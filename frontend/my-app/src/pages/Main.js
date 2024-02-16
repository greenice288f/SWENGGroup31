import React from 'react';
import { Link } from "react-router-dom";

function Main() {
    return (
        <>
            {/* temp links */}
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/sentimental">Sentimental Analysis</Link>
                </li>
                <li>
                    <Link to="/image">Image Analysis</Link>
                </li>
            </ul>
        </>
    );
}

export default Main;