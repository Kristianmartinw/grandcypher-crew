import React from 'react';
import './characters.css';


const Characters = ({ characters }) => {


    console.log('THIS IS CHARACTERS ----->', characters)

    return (
        <>
            <div className='characters-page'>
                This is characters page
            </div>
            {characters.map(character =>
                <div className='character-card'>
                    <div className='character-name'>
                        {character.name}
                    </div>
                    <div>
                        <img className='character-img' src={character.character_url}></img>
                    </div>
                </div>
            )}
        </>
    )
}

export default Characters;
