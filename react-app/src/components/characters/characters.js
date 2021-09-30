import React from 'react';
import { useSelector } from 'react-redux';
import './characters.css';


const Characters = ({ characters }) => {

    const elements = useSelector(state => state.elements)
    const races = useSelector(state => state.races)
    const specialties = useSelector(state => state.specialties)

    console.log('THIS IS CHARACTERS ----->', characters)

    return (
        <>
            <div className='characters-page'>
                {characters.map(character =>
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
                )}
            </div>
        </>
    )
}

export default Characters;
