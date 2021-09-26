const LOAD_RACES = "roles/LOAD_RACES"

const loadRaces = (races) => ({
    type: LOAD_RACES,
    races
});

export const getRaces = () => async (dispatch) => {
    const response = await fetch('/api/races/')

    if (response.ok) {
        const races = await response.json()
        dispatch(loadRaces(races))
        return
    }
    return
}

const initialState = {}

const racesReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_RACES: {
            return { ...action.races }
        }
        default:
            return state
    }
}

export default racesReducer
