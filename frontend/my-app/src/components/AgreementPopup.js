import React from 'react';
import ReactModal from 'react-modal';
import "./AgreementPopup.css";

class AgreementPopup extends React.Component {
    constructor () {
        super();
        this.state = {
            showModal: true
        };
        if ( localStorage.getItem('user_agreed') === "true" ) {
            this.state = {
                showModal: false
            };
        } else {
            this.state = {
                showModal: true
            };
        }

        this.handleOpenModal = this.handleOpenModal.bind(this);
        this.handleCloseModal = this.handleCloseModal.bind(this);
    }
    
    handleCloseModal () {
        this.setState({ showModal: false });
        this.agree();
    }

    handleOpenModal () {
        this.setState({ showModal: true });
    }

    agree() {
        localStorage.setItem('user_agreed', JSON.stringify(true));
        this.setState = {
            showModal: false
        };
    }

    render () {
        return (
            <ReactModal isOpen={this.state.showModal} shouldCloseOnOverlayClick={false} modal nested>
                    <div className='modal'>
                        <h1 className='priv-notice-title'>Privacy Notice</h1>
                        <hr/>
                        <p className='priv-notice-text'>By using this program, you agree that you are the owner of or have permission to analyze, the data provided.</p>
                        <button className='agree' onClick={this.handleCloseModal}>Agree</button>
                    </div>
            </ReactModal>
        )
    }
}

export default AgreementPopup