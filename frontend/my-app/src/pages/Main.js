import React from 'react';
import Header from '../components/Header';
import AgreementPopup from '../components/AgreementPopup';

function Main () {

    return (
        <>
            <Header></Header>
            <AgreementPopup></AgreementPopup>
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