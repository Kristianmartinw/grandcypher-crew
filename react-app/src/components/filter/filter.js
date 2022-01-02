import React, { useEffect, useState } from 'react';
import './filter.css';

const Filter = ({ characters, setFilteredCharacters, elements }) => {

    const [searchQuery, setSearchQuery] = useState('')
    const [selectedElement, setSelectedElement] = useState(new Array(elements.length - 1).fill(false))

    const updateSearchQuery = e => {
        setSearchQuery(e.target.value)
    }

    const updateSelectedElements = e => {
        const i = +e.currentTarget.id
        let updatedElement = [...selectedElement]
        updatedElement[i] = !updatedElement[i]
        setSelectedElement(updatedElement)
    }

    useEffect(() => {
        let filteredCharacters = [...characters]
        if (searchQuery.length) {
            filteredCharacters = filteredCharacters.filter(character => {
                return character.name.toLowerCase().includes(searchQuery.toLowerCase())
            })
        }
        if (selectedElement.includes(true)) {
            filteredCharacters = filteredCharacters.filter(character => {
                return selectedElement[+character?.element_id - 1]
            })
        }
        setFilteredCharacters(filteredCharacters)
    }, [searchQuery, selectedElement])

    return (
        <>
            <div className='filter-box'>
                <input value={searchQuery} onChange={updateSearchQuery} />
                <div className='elements-div element-selector'>
                    Element:
                    {elements.map((element, i) =>
                        i < 6 &&
                        <div className={selectedElement[i] ? 'selected elements' : 'elements'} id={i} onClick={updateSelectedElements}>
                            <img alt='elements' id={element.element_url} src={element.element_url}></img>
                        </div>
                    )}
                </div>
            </div>
        </>
    )
}

export default Filter;
