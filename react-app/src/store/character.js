const LOAD_CHARACTERS = "roles/LOAD_CHARACTERS"

const loadCharacters = (characters) => ({
    type: LOAD_CHARACTERS,
    characters
});

export const getCharacters = () => async (dispatch) => {
    const response = await fetch('/api/characters/')

    if (response.ok) {
        const characters = await response.json()
        dispatch(loadCharacters(characters))
        return
    }
    return
}

const initialState = {}

const charactersReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_CHARACTERS: {
            return { ...action.characters }
        }
        default:
            return state
    }
}

export default charactersReducer
