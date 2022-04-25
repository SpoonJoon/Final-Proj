# Sprint 1 Meeting Notes


**Attended**: Joonhwan, Dylan, Barrett

***

## Sprint Review

###  User Story:

As a client, I want an application that I can deploy on any server running Docker

### Sprint Requirements Attempted

**The application shall minimize required dependencies**
In order to minimize dependencies, we will containerize the application with its dependencies. 
Limit the dependency to a system that supports Docker containers.
*Status: completed*

### Completed Requirements

- implemented a flask web server
= Implemented a web page that displays hello world
  
### Incomplete Requirements

-  Postres DB (supplemented with a TinyDB database temporarily)

### The summary of the entire project:

<< A broad general overview of the entire project >>

- A web application that utilizes spaced repitition for efficient leet code sessions
- For more info please read planning/opening_ceremony.txt
- Currently have implemented a flask web server that displays hello world

***

## Sprint Planning

## Technical Flex

0/5 requirement flexes

## Technical Debt

- N/A (technical flex begins next week after further clarification from Professor Moore)

### Requirements Target:

- Add the Postgres database to our working Flask application, merging it with our docker-compose file
- Fully update the Software Requirements Specification document with requirements being implemented for the upcoming sprint.

### User Stories:

- As a client, I want an application that can handle a large number of users such that those that want to access the application/create a profile are not limited by the amount of users currently on the system.

### Planning

- Implement Postgres by using its official image and create separate Docker container 

### Action Items:

- Find and add the official Postgres image to the docker-compose file
- Build the container and communicate via the network specified in the docker-compose

### Issues and Risks:

- Difficulty integrating Postgres with the current application architecture.
    - Studying flask application architecture more in-depth and/or setting up an office hour meeting with the professor.

### Team Work Assignments:

<< A list of each team member and their works assignments for this sprint >>
#### Barret
- Add the Postgres image under db in the docker-compose
#### Joonhwan
- Set up networks in docker-compose for the db and app
#### Dylan
- Get data from the Postgres db and display on front-end
