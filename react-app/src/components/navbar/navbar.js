import React from 'react';
import { NavLink } from 'react-router-dom';
import DemoButton from '../auth/DemoButton';
import LogoutButton from '../auth/LogoutButton';
import SignupModal from '../auth/signUpModal';
import LoginModal from '../auth/loginModal';
import './navbar.css';

function Navbar({ sessionUser, authenticated }) {


    return (
        <>
            <div className='nav-containception'>
                <div className='nav-container'>
                    <img className='logo' alt='' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/gbf-logo.png'}></img>
                    {/* <img className='cloud-one' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/cloud.png'}></img>
            <img className='cloud-two' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/cloud-2.png'}></img>
            <img className='ship' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/ship.png'}></img>
            <img className='ship-two' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/ship-2.png'}></img>
            <img className='ship-three' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/ship-3.png'}></img>
            <img className='ship-four' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/ship-4.png'}></img> */}
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
                                    <img alt='' className='nav-url' src={sessionUser?.profile_url} />
                                </NavLink>
                                <LogoutButton />
                            </>
                    }

                </div >
            </div>
            <div className='something'>
                <NavLink to='/about-me' className='about-us'>
                    Click here to find out more <span className='about-me-link'>about me</span>
                </NavLink>
            </div>
        </>
    );
}

export default Navbar;
