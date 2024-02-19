import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../components/Header';

function Main () {

    return (
        <>
            <Header></Header>
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                paddingTop: '40px' /* header */
            }}>
                <h1>Welcome!</h1>
            </div>
        </>
    );
}

export default Main;