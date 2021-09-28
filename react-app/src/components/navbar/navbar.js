import React from 'react';
import { NavLink } from 'react-router-dom';
import DemoButton from '../auth/DemoButton';
import LogoutButton from '../auth/LogoutButton';
import './navbar.css';

function Navbar({ sessionUser, authenticated }) {


    return (
        <div className='nav-container'>

            <button>
                <NavLink to='/' exact={true} activeClassName='active'>
                    Home
                </NavLink>
            </button>
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
            {!authenticated ?
                <>
                    <button>
                        <NavLink to='/sign-up' exact={true} activeClassName='active'>
                            Sign Up
                        </NavLink>
                    </button>
                    <button>
                        <NavLink to='/login' exact={true} activeClassName='active'>
                            Login
                        </NavLink>
                    </button>
                    <DemoButton />
                </>
                :
                <>
                    <NavLink to={`/users/${sessionUser.id}`} exact={true} activeClassName='active'>
                        <img className='nav-url' src={sessionUser?.profile_url} />
                    </NavLink>
                    <LogoutButton />
                </>
            }

        </div>
    );
}

export default Navbar;
