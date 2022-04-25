# Sprint Meeting Notes

**Attended**: Barrett, Dylan, Joon

**DATE**: 3/23/2022

***

## Sprint 2 Review

### SRS Sections Updated

Two functional requirements were added to the SRS: React Client and Different Webpages.
This leaves us with a total of five requirements as needed by this appropriate milestone

Additionally, the Application Structure Diagram was added to the SRS, as well as the class structure diagram.

### User Story

As a client, I want an application that allows for users to be created and stored based on a given interface, so that information about users can be remembered and recalled

As a client, I want users to be able to input their own information into a system to be recorded long term, so that the user system of the application is dynamic and accounts for allowing any physical individual to have a profile on an application

As a client, I want an application that can store data in one location for a long term duration of time, so that data that will eventually be associated with users of the application will be maintained and organized in a fashion that it can be analyzed and optimized for fast retrieval.

### Sprint Requirements Attempted

We attempted three SRS requirements in the last sprint:

User Definition
User Input Signup
Database Schema

### Completed Requirements

User Definition and User Input Signup were completed in full.
Database Schema is mostly finished.

### Incomplete Requirements

The only part of the Database Schema that is not finished is the ability for long term storage through volumes.
Barrett reached out to the TA to get assistance in determining that the data persists in the database.
The TA claimed that the data persisted on his end when he attempted storing data, but we still can't seem to achieve it on our end.
We will be reaching out to the Professor and TA for additional help because in theory, the volumes should be working accordingly based on what we have written.

### The summary of the entire project

On top of all of the dockerized containers, we have an active webpage running that displays some basic text. Additionally, we have implemented a basic user class that is responsible for storing information of the user, and on localhost:5000/make_user, we have the ability to enter username and email information to be stored in the user class. More information will be associated with the user in the future. Multiple users can be added, and they are accurately reflected in the database. In the background, we have
began to define other potential classes that are going to be stored in the database, but they are not yet fully written and need to be further developed upon.

***

## Sprint 3 Planning

## Requirements Flex

5/5 requirement flexes remaining

## Technical Debt

If the volume issue regarding the database persistance counts as technical debt, then yes, we must take a technical debt point to finish that functionality.
However, it could be working and we are not accessing the database properly to check in on this capability. To be discussed during the sprint meeting.

### Requirement Target

We want to attempt two requirements from the SRS:

React Client
Different Webpages
(Finishing Database Schema if problem listed above is not as quick of a fix as expected)

### User Stories

As a client, I want a graphically enticing and effective user interface that allows for easy navigation of a website, so that any user who encounters the site will be able to navigate the appropriate buttons, processes, and services that the site has to offer without difficulty.

As a client, I want to be able to separate all information associated with a website into different subpages, so that when a user needs to look for a particular piece of information, they don’t have to search one long list of information on a page but instead can access the appropriate subpage of the site with ease.

### Planning

As always, we will meet Thursday night at 7 p.m. to discuss responsibilities and actively code/update documents.

### Action Items

More research must be performed about React in order to effectively know what options we can implement in terms of a graphical interface.
We must meet with the Professor/TA in order to discuss the data persistance issue, but we will continue developing our database schema as more classes are added.
More webpages are to be added, which requires us to plan out the particular webpages we want to have on the site, what we want to label them, and how we want to access them (buttons through Flask/React most likely).

### Issues and Risks

The only potential issue currently seen is the data persistance issue mentioned above. It could be a bug that data is not persisting in the volume; however, that is precisely why we will be meeting with the Prof/TA to hopefully resolve this issue.

### Team Work Assignments

Dylan: Continue to update the SRS with upcoming requirements. Use React to begin developing a more graphically pleasing user interface, displaying any current information on the front end. Work with Barrett and Joon to get an understanding of what classes are being added on the back end and what webpages are going to be used.

Joon and Barrett: Continue working on class designs, and associate these class designs with the database schema. Provide the necessary information that will ultimately be displayed on the front end to Dylan, so that he is actively able to display it