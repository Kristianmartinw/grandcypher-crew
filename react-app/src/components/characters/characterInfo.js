import React from "react";

function CharacterInfo({ character }) {

    return (
        <div className='character-info'>
            <img src={character.character_url} />
        </div>
    )
}

export default CharacterInfo;
