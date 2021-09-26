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
    const response = await fetch('/api/parties/')

    if (response.ok) {
        const parties = await response.json()
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
