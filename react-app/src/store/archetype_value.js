const LOAD_ARCHETYPE_VALUES = "archetype_value/LOAD_ARCHETYPE_VALUES"

const loadArchetypeValues = (archetypeValues) => ({
    type: LOAD_ARCHETYPE_VALUES,
    archetypeValues
});

export const getArchetypeValues = () => async (dispatch) => {
    const response = await fetch('/api/archetype_values/')

    if (response.ok) {
        const archetypeValues = await response.json()
        dispatch(loadArchetypeValues(archetypeValues))
        return
    }
    return
}

const initialState = {}

const archetypeValuesReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_ARCHETYPE_VALUES: {
            return { ...action.archetypeValues }
        }
        default:
            return state
    }
}

export default archetypeValuesReducer
