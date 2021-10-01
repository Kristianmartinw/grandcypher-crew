import React from 'react';
import { NavLink } from 'react-router-dom';
import DemoButton from '../auth/DemoButton';
import LogoutButton from '../auth/LogoutButton';
import SignupModal from '../auth/signUpModal';
import LoginModal from '../auth/loginModal';
import './navbar.css';

function Navbar({ sessionUser, authenticated }) {


    return (
        <div className='nav-container'>
            <img className='logo' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/gbf-logo.png'}></img>
            <NavLink to='/about-me' className='about-us'>
                Click here to find out more <span className='about-me-link'>about me</span>
            </NavLink>
            <button>
                <NavLink to='/parties' exact={true} activeClassName='active'>
                    Browse Parties
                </NavLink>
            </button>
            <button>
                <NavLink to='/characters' exact={true} activeClassName='active'>
                    Browse Characters
                </NavLink>
            </button>
            {
                !authenticated ?
                    <>
                        <SignupModal />
                        <LoginModal />
                        <DemoButton />
                    </>
                    :
                    <>
                        <span className="welcome-text">Welcome back, <span id="username">{sessionUser?.username}</span></span>
                        <NavLink to={`/users/${sessionUser.id}`} exact={true} activeClassName='active'>
                            <img className='nav-url' src={sessionUser?.profile_url} />
                        </NavLink>
                        <LogoutButton />
                    </>
            }

        </div >
    );
}

export default Navbar;
