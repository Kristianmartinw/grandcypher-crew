import React from 'react';
import './parties.css';

const Parties = ({ parties }) => {

    return (
        <>

            <div className='parties-page'>
                This is the parties page
            </div>
            {parties.map(party =>
                <div>
                    {party.name}
                </div>
            )}
        </>
    )
}

export default Parties;
