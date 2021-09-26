const LOAD_ARCHETYPES = "archetypes/LOAD_ARCHETYPE"

const loadArchetypes = (archetypes) => ({
    type: LOAD_ARCHETYPES,
    archetypes
});

export const getArchetypes = () => async (dispatch) => {
    const response = await fetch('/api/archetypes/')

    if (response.ok) {
        const archetypes = await response.json()
        dispatch(loadArchetypes(archetypes))
        return
    }
    return
}

const initialState = {}

const archetypesReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_ARCHETYPES: {
            return { ...action.archetypes }
        }
        default:
            return state
    }
}

export default archetypesReducer
