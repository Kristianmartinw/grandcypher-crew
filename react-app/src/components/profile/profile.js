import React, { useState, useEffect } from 'react';
import './profile.css';
import { useDispatch, useSelector } from "react-redux";
import CharacterCard from '../characters/CharacterCard';
import { createNewParty, editParty, deleteParty, addCharacterParty, deleteCharacterParty } from '../../store/party';
import ElementSelectModal from '../elements/elementModal';

const Profile = ({ parties, characters, elements }) => {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user);
    const usersParties = parties?.filter(party => party.owner_id === +sessionUser.id)

    const [partyName, setPartyName] = useState('')
    const [createParty, setCreateParty] = useState(false)
    const [selectParty, setSelectParty] = useState(usersParties[0]?.id)
    const [changeParty, setChangeParty] = useState(false)
    const [removeParty, setRemoveParty] = useState(false)
    const [currentCharacter, setCurrentCharacter] = useState('')
    const [addCharacter, setAddCharacter] = useState(false)
    const [editCharacter, setEditCharacter] = useState(false)
    const [showElementModal, setShowElementModal] = useState(false)
    const [elementSetter, setElementSetter] = useState(false)
    const [elementOne, setElementOne] = useState(false)
    const [elementTwo, setElementTwo] = useState(false)
    const [elementThree, setElementThree] = useState(false)
    const [elementFour, setElementFour] = useState(false)
    const [elementFive, setElementFive] = useState(false)
    const [elementSix, setElementSix] = useState(false)

    const party = usersParties?.find(party => party.id === +selectParty)
    const partyCharacterIds = party?.characters.map(character => character.id)
    const validCharacters = characters?.filter(character => !partyCharacterIds?.includes(character?.id))
    const [selectCharacter, setSelectCharacter] = useState(validCharacters[0]?.id)
    const currentCharacterName = characters[currentCharacter - 1]?.name

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

    const handleShowCreateParty = e => {
        setCreateParty(true)
        setPartyName('')
    }

    const handleShowEditParty = e => {
        setChangeParty(true)
        setPartyName(party?.name)
    }

    const handlePartyRemove = e => {
        e.preventDefault();
        dispatch(deleteParty(selectParty))
        setSelectParty(false)
        setRemoveParty(false)
    }

    const handleDefaultAddCharacter = e => {
        setAddCharacter(true)
        setSelectCharacter(validCharacters[0]?.id)
    }

    const handleDefaultEditCharacter = e => {
        setEditCharacter(true)
        setSelectCharacter(validCharacters[0]?.id)
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

    const handleSelectElement = e => {
        setElementSetter(e.currentTarget.className)
        setShowElementModal(true)
    }

    useEffect(() => {
        setCurrentCharacter('')
    }, [selectParty])

    return (
        <>
            <div className='party-scroll'>
                <div className='profile-page'>
                    <div className='profile-session'>
                        <img className='profile-img' src={sessionUser?.profile_url} />
                        <span className='session-name'>
                            {sessionUser?.username}
                        </span>
                    </div>
                    <div className='parties-info'>
                        <div className='select-party-text'> Select a party:</div>
                        <div className='profile-party-names'>
                            {usersParties.map(party =>
                                <div id={party.id} className='profile-party-name' onClick={e => setSelectParty(e.target.id)}>
                                    {party.name}
                                </div>
                            )}
                        </div>
                        <div className='party-buttons'>
                            {usersParties.length < 6 &&
                                < button onClick={handleShowCreateParty}>Create Party</button>
                            }
                            {createParty &&
                                <div>
                                    <form onSubmit={handlePartySubmit}>
                                        <input maxLength={10} value={partyName} onChange={e => setPartyName(e.target.value)} placeholder='Enter party name' required></input>
                                        <button>Submit</button>
                                    </form>
                                    <button onClick={e => setCreateParty(false)}>Cancel</button>
                                </div>
                            }
                            {usersParties.length > 0 && selectParty &&
                                <button onClick={handleShowEditParty}>Edit Party</button>
                            }
                            {changeParty && selectParty &&
                                <div>
                                    <form onSubmit={handleEditParty}>
                                        <input maxLength={10} onChange={e => setPartyName(e.target.value)} placeholder={partyName} required></input>
                                        <button>Submit</button>
                                    </form>
                                    <button onClick={e => setChangeParty(false)}>Cancel</button>
                                </div>
                            }
                            {usersParties.length > 0 && selectParty &&
                                <button onClick={e => setRemoveParty(true)}>Delete Party</button>
                            }
                            {removeParty && selectParty &&
                                < div >
                                    <form onSubmit={handlePartyRemove}>
                                        <button>Delete</button>
                                    </form>
                                    <button onClick={e => setRemoveParty(false)}>Cancel</button>
                                </div>
                            }
                        </div>
                        {selectParty &&
                            <>
                                <div className='profile-party'>
                                    <div className='party-name'>{party?.name}</div>
                                    {currentCharacterName &&
                                        <div className='selected-character-name'>
                                            Selected Character: {currentCharacterName}
                                        </div >
                                    }
                                    {/* {showElementModal && elementSetter === 'element-one' &&
                                        <ElementSelectModal elementSetter={setElementOne} elements={elements} setShowModal={setShowElementModal} />
                                    }
                                    {showElementModal && elementSetter === 'element-two' &&
                                        <ElementSelectModal elementSetter={setElementTwo} elements={elements} setShowModal={setShowElementModal} />
                                    }
                                    {showElementModal && elementSetter === 'element-three' &&
                                        <ElementSelectModal elementSetter={setElementThree} elements={elements} setShowModal={setShowElementModal} />
                                    }
                                    {showElementModal && elementSetter === 'element-four' &&
                                        <ElementSelectModal elementSetter={setElementFour} elements={elements} setShowModal={setShowElementModal} />
                                    }
                                    {showElementModal && elementSetter === 'element-five' &&
                                        <ElementSelectModal elementSetter={setElementFive} elements={elements} setShowModal={setShowElementModal} />
                                    }
                                    {showElementModal && elementSetter === 'element-six' &&
                                        <ElementSelectModal elementSetter={setElementSix} elements={elements} setShowModal={setShowElementModal} />
                                    }
                                    <div className='element-selector'>
                                        <div onClick={handleSelectElement} className='element-one'>
                                            {elementOne &&
                                                <img src={elementOne}></img>
                                            }
                                        </div>
                                        <div onClick={handleSelectElement} className='element-two'>
                                            {elementTwo &&
                                                <img src={elementTwo}></img>
                                            }
                                        </div>
                                        <div onClick={handleSelectElement} className='element-three'>
                                            {elementThree &&
                                                <img src={elementThree}></img>
                                            }
                                        </div>
                                        <div onClick={handleSelectElement} className='element-four'>
                                            {elementFour &&
                                                <img src={elementFour}></img>
                                            }
                                        </div>
                                        <div onClick={handleSelectElement} className='element-five'>
                                            {elementFive &&
                                                < img src={elementFive}></img>
                                            }
                                        </div>
                                        <div onClick={handleSelectElement} className='element-six'>
                                            {elementSix &&
                                                <img src={elementSix}></img>
                                            }
                                        </div>
                                    </div> */}
                                    <div className='party-box'>
                                        <div className='character-select' onClick={e => setCurrentCharacter(party?.characters[0]?.id)}>
                                            <CharacterCard character={party?.characters[0]} />
                                        </div>
                                        <div className='character-select' onClick={e => setCurrentCharacter(party?.characters[1]?.id)}>
                                            <CharacterCard character={party?.characters[1]} />
                                        </div>
                                        <div className='character-select' onClick={e => setCurrentCharacter(party?.characters[2]?.id)}>
                                            <CharacterCard character={party?.characters[2]} />
                                        </div>
                                    </div>
                                </div>
                            </>
                        }
                    </div>
                    <div className='character-buttons'>
                        {selectParty && party?.characters.length < 3 &&
                            <button className='character-button' onClick={handleDefaultAddCharacter} >Add character</button>
                        }
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
                        {currentCharacter && selectParty &&
                            <button className='character-button' onClick={handleDefaultEditCharacter} disabled={!currentCharacter}>Change Character</button>
                        }
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
                        {currentCharacter && selectParty &&
                            <button className='character-button' onClick={e => handleRemoveCharacter()} disabled={!currentCharacter}>Remove Character</button>
                        }
                    </div>
                </div>
            </div>
        </>
    )
}

export default Profile;
