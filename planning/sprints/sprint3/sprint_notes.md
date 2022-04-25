# Sprint Meeting Notes

*note: replace anything surrounded by << >> and **remove** the << >>*

**Attended**: Dylan, Joonhwan, Barrett

**DATE**: 4/3/22

***

## Sprint 3 Review

### SRS Sections Updated

Our team roles were updated in the last sprint. Five more functional requirements were added to the SRS as well to be chosen for future sprints.
Testing information is also actively being added to the SRS for tonights milestone due date/time.

### User Story

As a client, I want a graphically enticing and effective user interface that allows for easy navigation of a website, so that any user who encounters the site will be able to navigate the appropriate buttons, processes, and services that the site has to offer without difficulty.

As a client, I want to be able to separate all information associated with a website into different subpages, so that when a user needs to look for a particular piece of information, they don’t have to search one long list of information on a page but instead can access the appropriate subpage of the site with ease.

### Sprint Requirements Attempted

React Client (renamed to Graphic Non-Textual Capability since the last sprint)
Different Webpages

### Completed Requirements

React Client (renamed to Graphic Non-Textual Capability since the last sprint)
Different Webpages

Upon loading the localhost on port 3000, we have an active react client application running to modify for future sprints in graphic development
We also have our main URL page to update with information for future sprint.
On top of that, we have our make_user page which will eventually be graphically enhanced for login. Users can actively sign up now with a username and email.

### Incomplete Requirements

No requirements were incomplete from the last sprint.

### The summary of the entire project

On top of all of the dockerized containers, we have an active webpage running that displays some basic text. Additionally, we have implemented a basic user class that is responsible for storing information of the user, and on localhost:5000/make_user, we have the ability to enter username and email information to be stored in the user class. More information will be associated with the user in the future. Multiple users can be added, and they are accurately reflected in the database. In the background, we have
began to define other potential classes that are going to be stored in the database, but they are not yet fully written and need to be further developed upon.

We have added React in the background to help with grapical development of our application. Database information is finally persisting across time once the container is closed, with the help of the professor/TA. We have a few templates in mind from React to implement that suits our usability pattern that we have designed within the last milestone.

***

## Sprint 4 Planning

## Requirements Flex

5/5 requirement flexes remaining

## Technical Debt

Not applicable

### Requirement Target

Problem Set Definition
Informative Landing Page
Navigation Bar

### User Stories

As an aspiring software engineer, I want a full breakdown of all the possible Leetcode patterns available to learn, grow, and choose from, so that I am not left with impartial knowledge of how much information I am going to need to know before starting technical interviews

As a client, I want users to understand exactly what the application is offering upon accessing the website, so that users don't join when it's not a service that they need or they do join when it is exactly what they need.

As a client, I want users to be able to find exactly what they need on the website in two clicks or less (settings, main features, profile, etc), so that they cannot get lost within the variety of services that will be offered by the application.

### Planning

We will be meeting this Thursday 4/7 to discuss assignments distributed amongst the team members, and we will also be meeting over the weekend to discuss any problems that we run into.

### Action Items

Find a template with a navigation bar and landing page for React
OR
Design one ourselves with buttons linking to different pages of the website

Compile a list of all of the Leetcode patterns, and determine what needs to be provided by the Problems class to the user (/in discussion with the database as well. Does this information even need to be stored in the database? Probably)

Determine the required functions with the Problem class (talk to the TA/Professor about specific designs for this class)

### Issues and Risks

Encorporating other react design templates to suit the navigation bar and landing page might be really helpful, but it may also prove to be very difficult merging our project with the template. In theory its possible given that we have React up and running, but we won't know the difficulty until we actually try implementing it.

### Team Work Assignments

Dylan - Work on front end development with React, develop the graphical interface/merging necessary features with Flask
Joon - Help with front end development with Dylan
Barrett - Compile the Leetcode problems together into one organized place to hopefully be displayed to the user moving forward

All - Develop the Problems class and work to encorporate some functionality into the actual application regarding problem sets.
