import React from 'react';
import CharacterCard from './CharacterCard';
import './characters.css';


const Characters = ({ characters }) => {

    return (
        <>
            <img className='parties-background' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/papyrus.png'}></img>
            <div className='characters-page'>
                {characters.map(character =>
                    <CharacterCard character={character} />
                )}
            </div>
        </>
    )
}

export default Characters;
