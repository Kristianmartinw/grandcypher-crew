const LOAD_PARTIES = "roles/LOAD_PARTIES"

const loadParties = (parties) => ({
    type: LOAD_PARTIES,
    parties
});

export const getParties = () => async (dispatch) => {
    const response = await fetch('/api/party/')

    if (response.ok) {
        const parties = await response.json()
        dispatch(loadParties(parties))
        return
    }
    return
}

const initialState = {}

const partiesReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_PARTIES: {
            return { ...action.parties }
        }
        default:
            return state
    }
}

export default partiesReducer
