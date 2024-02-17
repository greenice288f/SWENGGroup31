import React from 'react';
import { Link } from 'react-router-dom';

function Main () {

    return (
        <>
            {/* TODO: move these to css/make it look nicer */}
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                'flex-wrap': 'wrap',
                'padding-top': '20px'
            }}>
                <Link to='/image/'>CIGARETTE IMAGE DETECTION</Link>
            </div>
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                'flex-wrap': 'wrap',
                'padding-top': '20px'
            }}>
                <Link to='/sentimental/'>SENTIMENTAL ANALYSIS</Link>
            </div>
        </>
    );
}

export default Main;