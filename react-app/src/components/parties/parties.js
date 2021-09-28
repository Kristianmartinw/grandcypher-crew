import React, { useEffect } from 'react';
import './parties.css';
import { useDispatch, useSelector } from 'react-redux';
import { addRating, deleteRating, editParty, editRating } from '../../store/party'

const Parties = ({ parties }) => {

    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user);

    const handlePartyRating = e => {
        const ratingIdArray = e.target.id.split('-')
        const rating = +ratingIdArray[0]
        const partyId = +ratingIdArray[1]
        const party = parties.find(party => party.id === partyId)
        const userRating = party?.ratings.find(rating => rating.userId === sessionUser.id)

        if (!userRating) {
            dispatch(addRating({ value: rating, partyId, userId: sessionUser?.id }))
        } else {
            if (userRating?.value === rating) {
                dispatch(deleteRating(userRating.id))
            } else {
                dispatch(editRating({ value: rating, ratingId: userRating?.id }))
            }
        }
    }

    useEffect(() => {
        const stars = Array.from(document.querySelectorAll('.fa-star'))
        const fiveStar = stars.filter(star => star.id[0] === '5')
        fiveStar.forEach(star => {
            star.classList.add('five-star-filled')
        })
    })

    return (
        <>

            <div className='parties-page'>
                This is the parties page
            </div>
            <div className='user-party'>
                {parties.map(party =>
                    <>
                        <div>
                            {party?.name}
                        </div>
                        <div>
                            <i id={`1-${party.id}`} onClick={handlePartyRating} className={`${party?.ratings.find(rating => rating?.userId === sessionUser?.id)?.value >= 1 ? 'fas fa-star' : 'far fa-star'}`}></i>
                            <i id={`2-${party.id}`} onClick={handlePartyRating} className={`${party?.ratings.find(rating => rating?.userId === sessionUser?.id)?.value >= 2 ? 'fas fa-star' : 'far fa-star'}`}></i>
                            <i id={`3-${party.id}`} onClick={handlePartyRating} className={`${party?.ratings.find(rating => rating?.userId === sessionUser?.id)?.value >= 3 ? 'fas fa-star' : 'far fa-star'}`}></i>
                            <i id={`4-${party.id}`} onClick={handlePartyRating} className={`${party?.ratings.find(rating => rating?.userId === sessionUser?.id)?.value >= 4 ? 'fas fa-star' : 'far fa-star'}`}></i>
                            <i id={`5-${party.id}`} onClick={handlePartyRating} className={`${party?.ratings.find(rating => rating?.userId === sessionUser?.id)?.value >= 5 ? 'fas fa-star' : 'far fa-star'}`}></i>
                        </div>
                        {
                            party.characters.map(character =>
                                <img className='party-characters' src={character?.character_url}></img>
                            )
                        }
                    </>
                )}
            </div>
        </>
    )
}

export default Parties;
