const LOAD_SPECIALTIES = "roles/LOAD_SPECIALTIES"

const loadSpecialties = (specialties) => ({
    type: LOAD_SPECIALTIES,
    specialties
});

export const getSpecialties = () => async (dispatch) => {
    const response = await fetch('/api/specialties/')

    if (response.ok) {
        const specialties = await response.json()
        dispatch(loadSpecialties(specialties))
        return
    }
    return
}

const initialState = {}

const specialtiesReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_SPECIALTIES: {
            return { ...action.specialties }
        }
        default:
            return state
    }
}

export default specialtiesReducer
