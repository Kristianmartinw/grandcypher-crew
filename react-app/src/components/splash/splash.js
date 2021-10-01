import React from "react";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux'
import LoginModal from "../auth/loginModal";
import * as sessionActions from '../../store/session';
import "./splash.css"

function Splash() {

    const dispatch = useDispatch();
    useSelector(state => state.session.user)

    let credential = 'gran@blue.io'
    let password = 'password'
    let demoLogin = () => { return dispatch(sessionActions.login(credential, password)) }


    return (
        <div className="splashContainer">
            <h1 className="splashTitle">Grandcypher Crew Builder</h1>
            <h2 className="splashSub">Party building made easier so you can focus on soaring the limitless blue</h2>
            <div className="splashLinkDiv">
                <Link to="/sign-up" className="splashLinks">Sign up</Link>
                <Link to="/login" className="splashLinks">Log in</Link>
                <Link to="/parties" className="splashLinks">View Parties</Link>
                <Link to="/characters" className="splashLinks">View Characters</Link>
                <a className="splashLinks" onClick={demoLogin}>Demo</a>
            </div>
        </div>
    )
}

export default Splash
