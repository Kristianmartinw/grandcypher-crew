import React from 'react';
import { Modal } from '../../context/modal';
import ElementSelect from './elementSelect'

function ElementSelectModal({ elementSetter, elements, setShowModal }) {
    console.log('HERE AND THERE', elementSetter)
    return (
        <>

            <Modal onClose={() => setShowModal(false)} >
                <ElementSelect elementSetter={elementSetter} elements={elements} setShowModal={setShowModal} />
            </Modal>
        </>
    )
}

export default ElementSelectModal;
