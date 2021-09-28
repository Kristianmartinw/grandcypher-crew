import React, { useState } from 'react';
import './profile.css';
import { useDispatch, useSelector } from "react-redux";
import { createNewParty, editParty, deleteParty, addCharacterParty, deleteCharacterParty } from '../../store/party';

const Profile = ({ parties, characters }) => {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user);

    const [partyName, setPartyName] = useState('')
    const [createParty, setCreateParty] = useState(false)
    const [selectParty, setSelectParty] = useState(false)
    const [changeParty, setChangeParty] = useState(false)
    const [removeParty, setRemoveParty] = useState(false)
    const [selectCharacter, setSelectCharacter] = useState(1)
    const [addCharacter, setAddCharacter] = useState(false)
    const [removeCharacter, setRemoveCharacter] = useState(false)

    const party = parties?.find(party => party.id === +selectParty)
    const character = parties?.find(character => character.id)

    console.log('THIS IS CHARACTER ------>', character)

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
        setChangeParty(false)
    }

    const handlePartyRemove = e => {
        e.preventDefault();
        dispatch(deleteParty(selectParty))
        setRemoveParty(false)
    }

    const handleAddCharacter = e => {
        e.preventDefault()

        dispatch(addCharacterParty(party.id, selectCharacter))
        setAddCharacter(false)
    }

    const handleRemoveCharacter = e => {
        e.preventDefault();
        dispatch(deleteCharacterParty(party.id, selectCharacter))
        setRemoveCharacter(false)
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
                        <input value={partyName} onChange={e => setPartyName(e.target.value)} placeholder='Enter party name' Required></input>
                        <button>Submit</button>
                    </form>
                    <button onClick={e => setCreateParty(false)}>Cancel</button>
                </div>
            }
            <button onClick={e => setChangeParty(true)}>Edit Party</button>
            {changeParty &&
                <div>
                    <form onSubmit={handleEditParty}>
                        <input onChange={e => setPartyName(e.target.value)} Required></input>
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
            <button onClick={e => setAddCharacter(true)}>Add character</button>
            {addCharacter && selectParty &&
                < div >
                    <form onSubmit={handleAddCharacter}>
                        <select value={selectCharacter} onChange={e => setSelectCharacter(e.target.value)}>
                            {characters.map(character =>
                                <option value={character.id}>
                                    {character.name}
                                </option>
                            )}
                        </select>
                        <button>Submit</button>
                    </form>
                    <button onClick={e => setAddCharacter(false)}>Cancel</button>
                </div>
            }
            <button>Change Character</button>
            <button onClick={e => setRemoveCharacter(true)}>Remove Character</button>
            {removeCharacter && selectParty &&
                <div>
                    <form onSubmit={handleRemoveCharacter}>
                        <select value={selectCharacter} onChange={e => setSelectCharacter(e.target.value)}>
                            {party.characters.map(character =>
                                <option value={character.id}>
                                    {character.name}
                                </option>
                            )}
                        </select>
                        <button>Submit</button>
                    </form>
                    <button onClick={e => setRemoveCharacter(false)}>Cancel</button>
                </div>
            }
        </>
    )
}

export default Profile;
