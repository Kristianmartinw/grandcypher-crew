import React from 'react';
import './characters.css';


const Characters = ({ characters }) => {


    console.log('THIS IS CHARACTERS ----->', characters)

    return (
        <>
            <div className='characters-page'>
                This is characters page
            </div>

            {characters.map(character => <img src={character.character_url}></img>)}

        </>
    )
}

export default Characters;
