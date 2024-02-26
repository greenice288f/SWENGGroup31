import React from 'react';
import ReactModal from 'react-modal';

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
                        <h1>Privacy Notice</h1>
                        <p>By using this program, you agree that you are the owner of or have permission to analyze, the data provided.</p>
                        <button onClick={this.handleCloseModal}>Agree</button>
                    </div>
            </ReactModal>
        )
    }
}

export default AgreementPopup