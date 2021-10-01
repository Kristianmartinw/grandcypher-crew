import React from "react";
import { useSelector } from "react-redux";

function CharacterCard({ character }) {

    const elements = useSelector(state => state.elements)

    return (
        <div className='character-card'>
            <div className='character-name'>
                {character?.name || 'Click to select character'}
            </div>
            <div className='character-img-container'>
                {character &&
                    <img id={`character-${character?.id}`} className='character-img' src={character?.character_url}></img>
                }
            </div>
            <div className='character-element-container'>
                {character &&
                    <img className='character-element' src={elements[character?.element_id]?.element_url}></img>
                }
            </div>
        </div>
    )
}

export default CharacterCard;
