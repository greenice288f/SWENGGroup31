import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import AgreementPopup from '../components/AgreementPopup';

function Main () {

    return (
        <>
            <Header></Header>
            <AgreementPopup></AgreementPopup>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                paddingTop: 130, /* Remove later -> made for demo sake*/
                paddingBottom: 250, /* Remove later -> made for demo sake*/
                justifyContent: 'center',
            }}>
                <h1>Welcome!</h1>
            </div>
            <Footer></Footer>
        </>
    );
}

export default Main;