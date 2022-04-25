# Sprint 1 Meeting Notes


**Attended**: Dylan, Barrett, Joonhwan

***

## Sprint Review



### SRS Sections Updated

Requirements section was added to the SRS after the introduction, and two functional and one non-functional were updated.
Some basic information was added as well, such as github repository, names, etc.

###  User Story:

As a client, I want an application that can handle a large number of users such that those that want to access the application/create a profile 
are not limited by the amount of users currently on the system.

### Requirement Implemented

Non-Functional Requirement: Dockerization
  - Create a dockerized environment with Flask and Postgres containers that will enable future handling of both collecting, storing, and outputting user data.

### Completed Items

Postgres was added as its own container to be used for future sprint. Also, the SRS was updated with the initial first three requirements.

### Uncompleted Items

No work was left uncompleted.

### The summary of the entire project:

Currently, we have a dockerized container of flask ready to display information on the front end, which we have finally added postgres in the background for future data storage.


***

## Sprint Planning

### Requirement Target:

1) User Definition
2) User Sign-Up Input
3) Database Schema

Please see SRS link for more information: https://docs.google.com/document/d/11qr-TcnbpLEQwhJYZx_g-XojqWdXfPDrXPPvSStlQyQ/edit?usp=sharing

### User Stories:

- As a client, I want an application that allows for users to be created and stored based on a given interface, so that information about users can be remembered and recalled
- As a client, I want users to be able to input their own information into a system to be recorded long term, so that the user system of the application is dynamic and accounts for allowing any physical individual to have a profile on an application
- As a client, I want an application that can store data in one location for a long term duration of time, so that data that will eventually be associated with users of the application will be maintained and organized in a fashion that it can be analyzed and optimized for fast retrieval.

### Planning

We plan to continue to meet during class Wednesday 3/9 and Thursday 3/10 outside of class time. 
We also plan to meet over spring break on Thursday 3/17 in order to discuss progress on further action items and team work assignments.
For specific tasks each member will work on, check out Team Work Assignments.

### Action Items:

Create a python class that allows for instatiation of user fields associated with the profiles we want to create (first name, last name, email, etc)
Develop the Flask front end further with input text fields and submission boxes that map the information provided by the user to the user class instance.
Create a database schema ready to store the associated user information.
Tranfer the data stored in the user class to the database, and retrieve the data from the database to ensure that it is being stored properly.
Update the SRS with the additional requirements responsible for the milestone.
Update the SRS with the Software Architecture Diagrams, using LucidChart or other detailed design charts.

### Issues and Risks:

A potential issue that we may have is encountering errors when storing the user data from the front end to the back end/retrieving it in the opposite direction. 
Barrett has the most experience amongst the database queries, and he said he is willing to explain it more in depth to Dylan and Joonhwan.
Ultimately, the only true obstacle we see is the unpredictability of spring break schedules in terms of making times to meet,
although we have our own discord server to work out scheduling conflicts and am currently planning times to meet up.

### Team Work Assignments:

Dylan: Update the SRS with both requirements and software architecture diagram. Work with Barrett on the Flask input structure/data collection.
Joonhwan: Work with Barrett on the database implementation/schema design. Also begin future research on NGinx in the background
Barrett: Work on the database schema and flask input with Joonhwan and Dylan respectively
