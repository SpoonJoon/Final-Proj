# Sprint Meeting Notes

**Attended**: Dylan, Joonhwan, Barrett

**DATE**: 04/11/2022

***

## Sprint 4 Review

### SRS Sections Updated

User Interface Section
(will be completed by 11:59 p.m. tonight; follows heavily off of our usability milestone)

### User Story

As an aspiring software engineer, I want a full breakdown of all the possible Leetcode patterns available to learn, grow, and choose from, so that I am not left with impartial knowledge of how much information I am going to need to know before starting technical interviews

As a client, I want users to understand exactly what the application is offering upon accessing the website, so that users don't join when it's not a service that they need or they do join when it is exactly what they need.

As a client, I want users to be able to find exactly what they need on the website in two clicks or less (settings, main features, profile, etc), so that they cannot get lost within the variety of services that will be offered by the application.

### Sprint Requirements Attempted

Problem Set Definition  

Informative Landing Page  
Navigation Bar  

### Completed Requirements

Navigation Bar

Informative Landing page had progress made towards it, but is not finished.

### Incomplete Requirements

Problem Set Definition
Informative Landing Page

As far as the landing page goes, React opens up straight to our opening page with the navigation bar and potentially a pop up modal (although that needs to be on the dashboard page once completed). We just do not have the information of what our site hopes to accomplish posted to the landing page in a visually pleasing format yet.

We did not get to the problem set definitions. We have our Problems class ready to push that information to the database. None of us were able to achieve it this sprint, however, with other issues we were trying to solve both within the project and due to a busy week.

### The summary of the entire project

On top of all of the dockerized containers, we have an active webpage running that displays some basic text. Additionally, we have implemented a basic user class that is responsible for storing information of the user, and on localhost:5000/make_user, we have the ability to enter username and email information to be stored in the user class. More information will be associated with the user in the future. Multiple users can be added, and they are accurately reflected in the database. In the background, we have
began to define other potential classes that are going to be stored in the database, but they are not yet fully written and need to be further developed upon.

We have added React in the background to help with grapical development of our application. Database information is finally persisting across time once the container is closed, with the help of the professor/TA. 

As far as the interface goes, we have encorporated our navigation bar to bring us to different webpages on the site, with different landing pages to contain different information. From here, the user can access the different capabilities of the website once they are achieved.

***

## Sprint 5 Planning

## Requirements Flex

4 (or 2?)/5 requirement flexes remaining
(Does one flex apply for one requirement or an entire sprint?)

## Technical Debt

Problem Set Definition
Informative Landing Page

### Requirement Target

On Top of Technical Debt:
    Pop Up Tutorial
    Toggle Ability

### User Stories

As a client, I want users to have the ability to decide which Leetcode patterns they want to study and which ones they want to postpone for later studies, so that the user has some control of their learning path while also being directed by the application

As a client, I want users to be prompted with tutorialized information on how to use the application, so that users do not have to figure the services provided themselves but instead they are given the chance to be walked through exactly what is intended by the application

### Planning

Meet Thursday 4/14 and/or Friday 4/15 as a team in order to go over front end developement and speak about bringing the back end further into the display.

### Action Items

-Need to merge new React features into the front end, and also display more of the back end features on the front end for the user's access.

-Learn more about project structure and React to make it easier to add features to the front end modularly.

-Study the Leetcode API in order to understand how to tie its services into the backend and also work to associate it with our problem sets



### Issues and Risks

Learning about different react features, it may prove difficult to merge them into one project, as many tutorials about these capabilities are often starting from scratch with their own project design/setup. Not impossible to comprehend however. 

Bringing in the Leetcode API may provide restrictions when it comes to the user (whether they need to have the same email/login credentials, etc.)

### Team Work Assignments

Dylan - Bring together the design of the front end to put together the user interface as described by the SRS/Usability documents
Barrett and Joon - Developing the problem set definitions as well as working with the Leetcode API services in order to get a handle on the problem sets, such that they can be associated with the different Leetcode patterns.

