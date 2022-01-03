import React from 'react';
import CharacterCard from './CharacterCard';
import CharacterInfoModal from './characterModal';
import './characters.css';


const Characters = ({ characters }) => {

    return (
        <>
            <div className='party-scroll'>
                <div className='characters-page'>
                    {characters.map(character =>
                        <CharacterInfoModal key={character.id} character={character} />
                        // < CharacterCard key={character.id} character={character} />
                    )}
                </div>
            </div>
        </>
    )
}

export default Characters;
