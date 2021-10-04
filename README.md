# [grandcypher-crew](https://grandcypher-crew.herokuapp.com/)

Grandcypher-crew is an app that allows users to create a party of characters from the game Granblue Fantasy. 

## Development
* You can read more about the project using the wiki located at: https://github.com/Kristianmartinw/grandcypher-crew/wiki
* To start a development environment:
    1. Clone the repository at: https://github.com/Kristianmartinw/grandcypher-crew
    2. Run the command "npm install" from the react-app directory in your terminal to install dependencies for the front end
    3. Run the command "pipenv install" from the root directory in your terminal to install dependencies for the backend and create a virtual environment.
    4. Run the command "flask run" from the root directory to start the backend server.
    5. Run the command "npm start" from the react-app directory to start the frontend server.
    6. Navigate to the localhost port specified in config/index.js

## Technologies Used
* Javascript
* HTML/CSS
* Reactjs
* Python
* Node.js
* Flask
* Postgres
* Heroku
* Git/Github
* Redux

##  Features
* Users
    * User functionality including registration, Login/Logout authentication, and authorization to perform different CRUD operations throughout the site is all present.
    * User can create parties of different characters and also rate other uses parties.
    * On registration a user is assigned an image of currently 8 possible profile pictures.
* Parties
    * On the parties page, a user can view all full parties that every user has created and rate the ones they found the most useful.
* Characters
    * On the characters page, a user can view all the characters currently supported by the app.
* Profile
    * A user can create a party, change its name, as well as delete one.
    * A user can add a character to a party, change the character, or remove it.
    * A party doesn't get added to the parties page until a user adds 3 characters to it to complete the party.
 
## Challenges and Learnings
* The biggest challenge was definitely the design of the site. I wanted to give the feel of it a very rpg, grand adventure, type look that the game invokes in the player. I feel I've accomplished this and made it feel alive with the animations in the background.
* Adjusting the website to conform to smaller sizes was also a challenge but currently the supported view screens are 1920x1080, 1280x720, and iPad.
* I learned about animations and keyframes to get my background to feel more alive.

## Features to be implemented later: 
  * Elements
  - Parties will have elements assigned to them as in the game.
  * Search
  - User will be able to search character names which will be necessary going forward as scrolling through 800+ characters would be a bad user experience.
  * Autobuild
  - For user's that aren't too knowledgable abotu the game, I'd like to add an algorithm that calculates the best formation based on the criterias a user sets.
  * Character Info
  - When clicking a character on the characters page, it should open a modal that show's all of the character's info.
  and more to come!
  

## Bugs that are still being worked on: 
  - Still need to get the ship animations working on smaller screens

## Contributors
* [Kristian Martinez](https://github.com/Kristianmartinw) (kristianmartinw)
