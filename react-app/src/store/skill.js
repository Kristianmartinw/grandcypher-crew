const LOAD_SKILLS = "roles/LOAD_SKILLS"

const loadSkills = (skills) => ({
    type: LOAD_SKILLS,
    skills
});

export const getSkills = () => async (dispatch) => {
    const response = await fetch('/api/skills/')

    if (response.ok) {
        const skills = await response.json()
        dispatch(loadSkills(skills))
        return
    }
    return
}

const initialState = {}

const skillsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_SKILLS: {
            return { ...action.skills }
        }
        default:
            return state
    }
}

export default skillsReducer
