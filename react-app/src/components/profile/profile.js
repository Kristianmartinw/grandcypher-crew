import React, { useState } from 'react';
import './profile.css';
import { useDispatch, useSelector } from "react-redux";
import { createNewParty, editParty, deleteParty } from '../../store/party';

const Profile = ({ parties }) => {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user);

    const [partyName, setPartyName] = useState('')
    const [createParty, setCreateParty] = useState(false)
    const [selectParty, setSelectParty] = useState(false)
    const [changeParty, setChangeParty] = useState(false)
    const [removeParty, setRemoveParty] = useState(false)

    const party = parties?.find(party => party.id === +selectParty)

    const handlePartySubmit = e => {
        e.preventDefault();

        const payload = {
            userId: sessionUser?.id,
            name: partyName,
        }
        dispatch(createNewParty(payload))
        setPartyName('')
        setCreateParty(false)
    }

    const handleEditParty = e => {
        e.preventDefault()

        const payload = {
            partyId: party.id,
            name: partyName
        }
        dispatch(editParty(payload))
    }

    const handlePartyRemove = e => {
        e.preventDefault();
        dispatch(deleteParty(selectParty))
        setRemoveParty(false)
    }

    return (
        <>

            <div className='profile-page'>
                This is the profile page
            </div>

            {sessionUser?.username}
            <div>
                <img className='profile-img' src={sessionUser?.profile_url} />
            </div>
            <div>
                <div>
                    {parties.map(party =>
                        <div id={party.id} onClick={e => setSelectParty(e.target.id)}>
                            {party.name}
                        </div>
                    )}
                </div>
                {selectParty &&
                    party?.characters.map(character =>
                        <div>
                            <img src={character.character_url} />
                        </div>
                    )
                }
            </div>
            <button onClick={e => setCreateParty(true)}>Create Party</button>
            {createParty &&
                <div>
                    <form onSubmit={handlePartySubmit}>
                        <input value={partyName} onChange={e => setPartyName(e.target.value)} placeholder='Enter party name'></input>
                        <button>Submit</button>
                    </form>
                    <button onClick={e => setCreateParty(false)}>Cancel</button>
                </div>
            }
            <button onClick={e => setChangeParty(true)}>Edit Party</button>
            {changeParty &&
                <div>
                    <form onSubmit={handleEditParty}>
                        <input onChange={e => setPartyName(e.target.value)}></input>
                        <button>Submit</button>
                    </form>
                    <button onClick={e => setChangeParty(false)}>Cancel</button>
                </div>
            }
            < button onClick={e => setRemoveParty(true)}>Delete Party</button>
            {removeParty &&
                <div>
                    <form onSubmit={handlePartyRemove}>
                        <button>Delete</button>
                    </form>
                    <button onClick={e => setRemoveParty(false)}>Cancel</button>
                </div>
            }
            <button>Add character</button>
            <button>Change Character</button>
            <button>Remove Character</button>
        </>
    )
}

export default Profile;
