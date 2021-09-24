import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import archetypeValuesReducer from './archetype_value'
import archetypesReducer from './archetype'
import charactersReducer from './character'
import chargeAttacksReducer from './chargeAttack'
import elementsReducer from './element'
import partiesReducer from './party'
import racesReducer from './race'
import skillsReducer from './skill'
import specialtiesReducer from './specialty'
import supportSkillsReducer from './supportSkill'

const rootReducer = combineReducers({
  session,
  archetypeValues: archetypeValuesReducer,
  archetypes: archetypesReducer,
  characters: charactersReducer,
  chargeAttacks: chargeAttacksReducer,
  elements: elementsReducer,
  parties: partiesReducer,
  races: racesReducer,
  skills: skillsReducer,
  specialties: specialtiesReducer,
  supportSkills: supportSkillsReducer,
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
