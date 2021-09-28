import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import Navbar from './components/navbar/navbar';
import Home from './components/home/home';
import Splash from './components/splash/splash'
import Pagenotfound from './components/pagenotfound/pagenotfound';
import Characters from './components/characters/characters';
import Parties from './components/parties/parties';
import Profile from './components/profile/profile';
import { authenticate } from './store/session';
import { getArchetypeValues } from './store/archetype_value'
import { getArchetypes } from './store/archetype'
import { getCharacters } from './store/character'
import { getChargeAttacks } from './store/chargeAttack'
import { getElements } from './store/element'
import { getParties } from './store/party'
import { getRaces } from './store/race'
import { getSkills } from './store/skill'
import { getSpecialties } from './store/specialty'
import { getSupportSkills } from './store/supportSkill'
import './index.css';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session?.user)
  const authenticated = sessionUser !== null

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();


    dispatch(getArchetypeValues())
    dispatch(getArchetypes())
    dispatch(getCharacters())
    dispatch(getChargeAttacks())
    dispatch(getElements())
    dispatch(getParties())
    dispatch(getRaces())
    dispatch(getSkills())
    dispatch(getSpecialties())
    dispatch(getSupportSkills())
  }, [dispatch]);

  const archetypeValuesSlice = useSelector(state => state.archetypeValues)
  const archetypesSlice = useSelector(state => state.archetypes)
  const charactersSlice = useSelector(state => state.characters)
  const chargeAttacksSlice = useSelector(state => state.chargeAttacks)
  const elementsSlice = useSelector(state => state.elements)
  const partiesSlice = useSelector(state => state.parties)
  const racesSlice = useSelector(state => state.races)
  const skillsSlice = useSelector(state => state.skills)
  const specialtiesSlice = useSelector(state => state.specialties)
  const supportSkillsSlice = useSelector(state => state.supportSkills)


  const archetypeValues = Object.values(archetypeValuesSlice)
  const archetypes = Object.values(archetypesSlice)
  const characters = Object.values(charactersSlice)
  const chargeAttacks = Object.values(chargeAttacksSlice)
  const elements = Object.values(elementsSlice)
  const parties = Object.values(partiesSlice)
  const races = Object.values(racesSlice)
  const skills = Object.values(skillsSlice)
  const specialties = Object.values(specialtiesSlice)
  const supportSkills = Object.values(supportSkillsSlice)

  if (!loaded) {
    return null;
  }



  return (
    <BrowserRouter>
      <Navbar sessionUser={sessionUser} authenticated={authenticated} />
      <Switch>
        <Route path='/' exact={true} >
          <Home sessionUser={sessionUser} authenticated={authenticated} />
        </Route>
        <Route path='/' exact={true} >
          <Splash />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/users/:id' exact={true}>
          <Profile archetypeValues={archetypeValues} parties={parties} characters={characters} sessionUser={sessionUser} authenticated={authenticated} />
        </Route>
        <Route path='/characters' exact={true} >
          <Characters characters={characters} />
        </Route>
        <Route path='/parties' exact={true} >
          <Parties parties={parties} />
        </Route>
        <Route>
          <Pagenotfound />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
