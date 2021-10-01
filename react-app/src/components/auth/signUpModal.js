import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import SignUpForm from './SignUpForm'

function SignupModal() {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <button onClick={() => setShowModal(true)}>Register</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)} >
                    <SignUpForm setShowModal={setShowModal} />
                </Modal>
            )}
        </>
    )
}

export default SignupModal;
