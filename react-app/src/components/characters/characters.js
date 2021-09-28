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
                This is characters page
            </div>
            {characters.map(character =>
                <div className='character-card'>
                    <div className='character-name'>
                        {character?.name}
                    </div>
                    <div className='character-img-container'>
                        <img className='character-img' src={character?.character_url}></img>
                    </div>
                    <div>
                        {character?.max_hp}
                    </div>
                    <div>
                        {character?.max_atk}
                    </div>
                    <div>
                        <img src={elements[character.element_id]?.element_url}></img>
                    </div>
                    <div>
                        <img src={races[character.race_id]?.race_url}></img>
                    </div>
                    <div>
                        <img src={specialties[character?.specialty_id]?.specialty_url}></img>
                    </div>
                </div>
            )}
        </>
    )
}

export default Characters;
