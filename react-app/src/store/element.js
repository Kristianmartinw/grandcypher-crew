const LOAD_ELEMENTS = "roles/LOAD_ELEMENTS"

const loadElements = (elements) => ({
    type: LOAD_ELEMENTS,
    elements
});

export const getElements = () => async (dispatch) => {
    const response = await fetch('/api/element/')

    if (response.ok) {
        const elements = await response.json()
        dispatch(loadElements(elements))
        return
    }
    return
}

const initialState = {}

const elementsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_ELEMENTS: {
            return { ...action.elements }
        }
        default:
            return state
    }
}

export default elementsReducer
