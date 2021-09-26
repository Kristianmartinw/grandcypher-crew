const LOAD_CHARGE_ATTACKS = "roles/LOAD_CHARGE_ATTACKS"

const loadChargeAttacks = (chargeAttacks) => ({
    type: LOAD_CHARGE_ATTACKS,
    chargeAttacks
});

export const getChargeAttacks = () => async (dispatch) => {

    const response = await fetch('/api/charge_attacks/')


    if (response.ok) {
        const chargeAttacks = await response.json()
        dispatch(loadChargeAttacks(chargeAttacks))
        return
    }
    return
}

const initialState = {}

const chargeAttacksReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_CHARGE_ATTACKS: {
            return { ...action.chargeAttacks }
        }
        default:
            return state
    }
}

export default chargeAttacksReducer
