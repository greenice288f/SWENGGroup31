import React from 'react';
import { Link } from 'react-router-dom';

function Main () {

    return (
        <>
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                'flex-wrap': 'wrap',
                'padding-top': '20px'
            }}>
                <Link to='/image/'>CIGARETTE IMAGE DETECTION</Link>
            </div>
        </>
    );
}

export default Main;