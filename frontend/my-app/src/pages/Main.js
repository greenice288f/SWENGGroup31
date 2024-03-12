import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import AgreementPopup from '../components/AgreementPopup';

function Main () {

    return (
        <>
            <Header />
            <AgreementPopup />
            <div style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                paddingTop: "130px", /* Remove later -> made for demo sake*/
                paddingBottom: "300px", /* Remove later -> made for demo sake*/
                justifyContent: 'center',
            }}>
                <h1>Welcome!</h1>
            </div>
            <Footer />
        </>
    );
}

export default Main;