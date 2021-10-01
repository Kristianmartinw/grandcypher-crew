import React, { useEffect, useRef, useState, useContext } from 'react';
import ReactDOM from 'react-dom';
import './modal.css'

const ModalContext = React.createContext();
export function ModalProvider({ children }) {
    const modalRef = useRef();
    const [value, setValue] = useState();

    useEffect(() => {
        setValue(modalRef.current)
    }, []);

    return (
        <>
            <ModalContext.Provider value={value}>
                {children}
            </ModalContext.Provider>
            <div ref={modalRef} />
        </>
    )
}

export function Modal({ onClose, children, className = '' }) {
    const modalNode = useContext(ModalContext);
    if (!modalNode) return null;

    return ReactDOM.createPortal(
        <div className='modal'>
            <div className='modal-background' onClick={onClose} />
            <div id='modal-body' onClick={e => e.stopPropagation()} className={className}>
                <img className='modal-papyrus' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/auth-papyrus.png'}>
                </img>
                {children}
            </div>
        </div>,
        modalNode
    );
}
