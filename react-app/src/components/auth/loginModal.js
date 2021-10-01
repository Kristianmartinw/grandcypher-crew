import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import LoginForm from './LoginForm'

function LoginModal() {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <button onClick={() => setShowModal(true)}>Login</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)} >
                    <LoginForm setShowModal={setShowModal} />
                </Modal>
            )}
        </>
    )
}

export default LoginModal;
