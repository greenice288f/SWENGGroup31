import React from 'react';
import Header from '../components/Header';

function Main () {

    return (
        <>
            <Header></Header>
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
            }}>
                <h1>Welcome!</h1>
            </div>
        </>
    );
}

export default Main;