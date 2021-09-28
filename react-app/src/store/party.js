const LOAD_PARTIES = "parties/LOAD_PARTIES"
const UPDATE_PARTY = "parties/UPDATE_PARTY"
const DELETE_PARTY = "parties/DELETE_PARTY"

const loadParties = (parties) => ({
    type: LOAD_PARTIES,
    parties
});

const updateParty = (party) => ({
    type: UPDATE_PARTY,
    party
});

const removeParty = (id) => ({
    type: DELETE_PARTY,
    id
})


export const getParties = () => async (dispatch) => {
    const res = await fetch('/api/parties/')

    if (res.ok) {
        const parties = await res.json()
        dispatch(loadParties(parties))
        return
    }
    return
}

export const createNewParty = (data) => async (dispatch) => {
    const res = await fetch('/api/parties/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ owner_id: data.userId, name: data.name })
    });


    if (res.ok) {

        const updatedParty = await res.json();
        dispatch(updateParty(updatedParty))
    }
}

export const editParty = (data) => async (dispatch) => {
    const res = await fetch(`/api/parties/${data.partyId}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: data.name }),
    })
    const newParty = await res.json()

    if (res.ok) {
        dispatch(updateParty(newParty))
        return
    }
    return newParty
}

export const deleteParty = (id) => async (dispatch) => {
    const res = await fetch(`/api/parties/${id}/`, {
        method: 'DELETE'
    })
    if (res.ok) {
        dispatch(removeParty(id))
        return
    }
}

export const addCharacterParty = (partyId, characterId) => async (dispatch) => {
    let res = await fetch(`/api/parties/${partyId}/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ character_id: characterId })
    })

    let data

    if (res.ok) {
        data = await res.json()
        dispatch(updateParty(data))
    }
}

export const deleteCharacterParty = (partyId, characterId) => async (dispatch) => {
    let res = await fetch(`/api/parties/${partyId}/characters/${characterId}`, {
        method: 'DELETE'
    })
    let data
    if (res.ok) {
        data = await res.json()
        dispatch(updateParty(data))
    }
}

export const addRating = data => async (dispatch) => {

    const res = await fetch(`/api/ratings/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ value: data.value, party_id: data.partyId, user_id: data.userId })
    })

    if (res.ok) {
        const party = await res.json()
        dispatch(updateParty(party))
    }
}

export const editRating = data => async (dispatch) => {

    const res = await fetch(`/api/ratings/${data.ratingId}/`, {
        body: JSON.stringify(data.value),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
    })
    if (res.ok) {
        const party = await res.json()
        dispatch(updateParty(party))
    }
}

export const deleteRating = ratingId => async (dispatch) => {

    const res = await fetch(`/api/ratings/${ratingId}/`, {
        method: 'DELETE'
    })

    if (res.ok) {
        const party = await res.json()
        dispatch(updateParty(party))
    }
}



const initialState = {}

const partiesReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_PARTIES: {
            return { ...action.parties }
        }
        case UPDATE_PARTY: {
            if (!state[action.party.id]) {
                let copy = {
                    ...state,
                    [action.party.id]: action.party
                }
                return copy
            }
            return {
                ...state,
                [action.party.id]: {
                    ...state[action.party.id],
                    ...action.party
                }
            }
        }
        case DELETE_PARTY: {
            let copy = { ...state }
            delete copy[action.id]
            return copy
        }
        default:
            return state
    }
}

export default partiesReducer
