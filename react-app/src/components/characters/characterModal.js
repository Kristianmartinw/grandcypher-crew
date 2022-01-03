import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import CharacterInfo from './characterInfo';
import CharacterCard from './CharacterCard';

function CharacterInfoModal({ character }) {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <div onClick={() => setShowModal(true)}>
                <CharacterCard character={character} />
            </div>
            {showModal && (
                <Modal background={false} onClose={() => setShowModal(false)} >
                    <CharacterInfo character={character} setShowModal={setShowModal} />
                </Modal>
            )}
        </>
    )
}

export default CharacterInfoModal;
