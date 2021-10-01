import React from "react";
import { useSelector } from "react-redux";

function CharacterCard({ character }) {

    const elements = useSelector(state => state.elements)
    const races = useSelector(state => state.races)
    const specialties = useSelector(state => state.specialties)

    return (
        <div className='character-card'>
            <div className='character-name'>
                {character?.name}
            </div>
            <div className='character-img-container'>
                <img id={`character-${character?.id}`} className='character-img' src={character?.character_url}></img>
            </div>
            <div className='character-element-container'>
                <img className='character-element' src={elements[character.element_id]?.element_url}></img>
            </div>
        </div>
    )
}

export default CharacterCard;
