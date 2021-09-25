import React from 'react';
import './home.css';
import Splash from '../splash/splash'

const Home = ({ sessionUser, authenticated }) => {

    return (
        authenticated ?
            <>
                <div className='home-container'>
                    <h1 id="welcome-text">Welcome back, <span id="username">{sessionUser?.username}</span>.</h1>
                </div>

            </>
            :
            <Splash />
    )
}

export default Home;
