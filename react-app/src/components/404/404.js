import React from "react";
import { Link } from 'react-router-dom';
import "./PageNotFound.css"

function PageNotFound() {
    return (
        <>
            <img className='parties-background' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/papyrus.png'}></img>
            <div className='not-found-page'>
                <div className='pnf-container'>
                    <h1 className='pnf-alert'> Oh no! </h1>
                    <h3 className='pnf-text'>You seem to have fallen out of the sky.</h3>
                    <h3 className='pnf-error-text'>Page not found:</h3>
                    <h3 className='pnf-error-text-2'>Error Code: (404)</h3>
                    <h3 className='pnf-redirect'>Click <Link className='pnf-redirect-link' to='/parties'>here</Link> so we can get you back to drifting in the clouds.</h3>
                </div>
            </div>
        </>
    )
}

export default PageNotFound
