import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../components/Header';

function Main () {

    return (
        <>
            <Header></Header>
            {/* TODO: move these to css/make it look nicer */}
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                'flex-wrap': 'wrap',
                'padding-top': '60px'
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