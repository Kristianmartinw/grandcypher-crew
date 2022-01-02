import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import Navbar from './components/navbar/navbar';
import Splash from './components/splash/splash'
import PageNotFound from './components/404/404'
import Aboutme from './components/Aboutme/aboutMe'
import Characters from './components/characters/characters';
import Parties from './components/parties/parties';
import Profile from './components/profile/profile';
import Filter from './components/filter/filter';
import ProtectedRoute from './components/auth/ProtectedRoute'
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
      await dispatch(getArchetypeValues())
      await dispatch(getArchetypes())
      await dispatch(getCharacters())
      await dispatch(getChargeAttacks())
      await dispatch(getElements())
      await dispatch(getParties())
      await dispatch(getRaces())
      await dispatch(getSkills())
      await dispatch(getSpecialties())
      await dispatch(getSupportSkills())
      setLoaded(true);
    })();

  }, [dispatch]);

  const archetypeValuesSlice = useSelector(state => state.archetypeValues)
  const charactersSlice = useSelector(state => state.characters)
  const elementsSlice = useSelector(state => state.elements)
  const partiesSlice = useSelector(state => state.parties)

  const archetypeValues = Object.values(archetypeValuesSlice)
  const characters = Object.values(charactersSlice)
  const elements = Object.values(elementsSlice)
  const parties = Object.values(partiesSlice)

  const [filteredCharacters, setFilteredCharacters] = useState([])

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Navbar sessionUser={sessionUser} authenticated={authenticated} />
      <Switch>
        <Route path='/' exact={true} >
          <Splash />
        </Route>
        <ProtectedRoute path='/users/:id' exact={true}>
          <Profile archetypeValues={archetypeValues} parties={parties} elements={elements} characters={characters} sessionUser={sessionUser} authenticated={authenticated} />
        </ProtectedRoute>
        <Route path='/characters' exact={true} >
          <Filter elements={elements} characters={characters} setFilteredCharacters={setFilteredCharacters} />
          <Characters characters={filteredCharacters} />
        </Route>
        <Route path='/parties' exact={true} >
          <Parties parties={parties} />
        </Route>
        <Route path='/about-me'>
          <Aboutme />
        </Route>
        <Route>
          <PageNotFound />
        </Route>
      </Switch>
    </BrowserRouter >
  );
}

export default App;
