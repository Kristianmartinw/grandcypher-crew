import React from 'react';

const ElementSelect = ({ elementSetter, setShowModal, elements }) => {

    const handleSelectElement = e => {
        elementSetter(e.target.id)
        setShowModal(false)
    }

    return (
        <div className='element-selector'>
            {elements.map((element, i) =>
                i < 6 &&
                < div >
                    <img onClick={handleSelectElement} id={element.element_url} src={element.element_url}></img>
                </div>
            )
            }
        </div >
    )
};

export default ElementSelect;
