import React, { useState, useEffect } from 'react';
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
    const [currentCharacter, setCurrentCharacter] = useState('')
    const [addCharacter, setAddCharacter] = useState(false)
    const [editCharacter, setEditCharacter] = useState(false)

    const usersParties = parties?.filter(party => party.owner_id === +sessionUser.id)
    const party = usersParties?.find(party => party.id === +selectParty)
    const partyCharacterIds = party?.characters.map(character => character.id)
    const validCharacters = characters?.filter(character => !partyCharacterIds?.includes(character?.id))

    useEffect(() => {
        setSelectCharacter(validCharacters[0]?.id)
    })

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

    const handleEditCharacter = async e => {
        e.preventDefault()

        await dispatch(deleteCharacterParty(party.id, currentCharacter))
        dispatch(addCharacterParty(party.id, selectCharacter))
        setEditCharacter(false)
        setCurrentCharacter('')
    }

    const handleRemoveCharacter = () => {
        dispatch(deleteCharacterParty(party.id, currentCharacter))
        setCurrentCharacter('')
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
                    {usersParties.map(party =>
                        <div id={party.id} onClick={e => setSelectParty(e.target.id)}>
                            {party.name}
                        </div>
                    )}
                </div>
                {selectParty &&
                    party?.characters.map(character =>
                        <div>
                            <img id={character.id} className='party-characters' onClick={e => setCurrentCharacter(e.target.id)} src={character.character_url} />
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
            <button onClick={e => setAddCharacter(true)} disabled={party?.characters.length === 4}>Add character</button>
            {addCharacter && selectParty &&
                < div >
                    <form onSubmit={handleAddCharacter}>
                        <select value={selectCharacter} onChange={e => setSelectCharacter(e.target.value)}>
                            {validCharacters.map(character =>
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
            <button onClick={e => setEditCharacter(true)} disabled={!currentCharacter}>Change Character</button>
            {editCharacter &&
                <div>
                    <form onSubmit={handleEditCharacter}>
                        <select value={selectCharacter} onChange={e => setSelectCharacter(e.target.value)}>
                            {validCharacters.map(character =>
                                <option value={character.id}>
                                    {character.name}
                                </option>
                            )}
                        </select>
                        <button>Submit</button>
                    </form>
                    <button onClick={e => setEditCharacter(false)}>Cancel</button>
                </div>
            }
            <button onClick={e => handleRemoveCharacter()} disabled={!currentCharacter}>Remove Character</button>
        </>
    )
}

export default Profile;
