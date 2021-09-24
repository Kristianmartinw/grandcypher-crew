const LOAD_SUPPORT_SKILLS = "roles/LOAD_SUPPORT_SKILLS"

const loadSupportSkills = (supportSkills) => ({
    type: LOAD_SUPPORT_SKILLS,
    supportSkills
});

export const getSupportSkills = () => async (dispatch) => {

    const response = await fetch('/api/support_skill/')


    if (response.ok) {
        const supportSkills = await response.json()
        dispatch(loadSupportSkills(supportSkills))
        return
    }
    return
}

const initialState = {}

const supportSkillsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_SUPPORT_SKILLS: {
            return { ...action.supportSkills }
        }
        default:
            return state
    }
}

export default supportSkillsReducer
