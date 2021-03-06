import React from "react";
import CharacterInfoModal from "./characterModal";
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
                    <img id={`character-${character?.id}`} alt='' className='character-img' src={character?.character_url}></img>
                }
            </div>
            <div className='character-element-container'>
                {character &&
                    <img className='character-element' alt='' src={elements[character?.element_id]?.element_url}></img>
                }
            </div>
        </div>
    )
}

export default CharacterCard;
