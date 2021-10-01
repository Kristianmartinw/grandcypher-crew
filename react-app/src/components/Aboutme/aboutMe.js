import { Link } from 'react-router-dom';
import "./aboutMe.css"

export default function AboutMe() {
    return (
        <>
            <img className='parties-background' src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/papyrus.png'}></img>
            <div className='about-us-page'>
                <h1 className='about-me-title'>Hello and thank you for your interest in Grandcypher Crew!</h1>
                <div className='aboutus'>
                    <p className='body-text'>I've played Granblue Fantasy for a little over a year and as I obtain more characters I find myself struggling to keep up with all of the different strategies and combinations. Constantly asking other players for advice can get tiresome so I began looking for an app that would build a party for me based on filters I set. It didn't exist. Distraught but not down, I decided to make this app myself to not only provide myself with ease of access but to others as well!</p>
                    <div className='team-body'>
                        Click the logos below if you want to see my professional accounts:
                        <div className='team-cards'>
                            <div className='k-card'>
                                <div>
                                    <span><Link className='' to={{ pathname: 'https://github.com/Kristianmartinw' }} target='true'><img className='gitHubImage' alt="githubLogo" src='https://partylureawsbucket.s3.amazonaws.com/github.png'></img></Link></span>
                                    <span><Link className='' to={{ pathname: 'https://www.linkedin.com/in/kristian-martinez-40137b21b/' }} target='true'><img className='gitHubImage' alt="githubLogo" src='https://partylureawsbucket.s3.amazonaws.com/linkedin.png'></img></Link></span>
                                </div>
                                Kristian Martinez
                            </div>
                        </div>
                    </div>
                    <footer className='footer'>
                        <div className='footer-Content'>If you want to keep up with the development of this app, check out my <Link className='readme-link' to={{ pathname: 'https://github.com/Kristianmartinw/grandcypher-crew#readme' }} target='true'>README</Link> here!</div>
                    </footer>
                </div>
            </div>
        </>
    )
}
