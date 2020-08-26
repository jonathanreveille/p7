# This is project 7 of Openclassrooms - Grandpy Bot :snake:

## Ask a question to Grandpy and he will tell you a story about it !

### What is in this project ?
- Use of Flask Framework.
- Use of OOP and Python 3.7.
- Use of GoogleMaps and MediaWiki API services.
- Use of AJAX for interaction on frontend side.
- Use of JavaScript, HTML5, CSS3.
- Test Driven Development on python code side with pytest.
- Use GoogleMaps API services, and MediaWiki API services.
- Use of pipenv (virtual env.)
- Respect and follow recommendations from PEP8(style guide),
 PEP257(docformatter)

### The project
For this project we had to create a Flask application called Grandpy.
It's a bot that is personified as a grandfather, and he will answer 
to you in french about some location you have asked him about.

This involved creating the back end and the front end at different times.
Also, this project had to be done the TDD (Test Driven Development) way. 
Test should first be done before coding at any cost on the python modules. 
I have decided to use pytest for this project to create all test methods.

The backend side, or the server side, will retrieve data from the frontend side (client side)
in order to treat it, or to modify it, to finally send it back towards the frontend side once
the operation is done.
The frontend side handles what the user of the application can see, and which action
the application is set to allow the user to perform with.

Your questions and the bot's answers will stay on your screen, this will allow you to scroll
through it. But beware, nothing is saved, so as soon as you press the refresh
button of your favorite web browser, you will lose your search history at this very moment.


### Structure of the code
In the folder **test**, it will document to you every method that has
been coded in python for this project. Use of tests and mocks from the
the pytest library.
In the folder **models**, you will find the methods that were
tested in the test folder.
in the folder **flaskapp**, you will find the flask application.


###  Getting started

If you want to run this project, clone this project,
but you will need to get on your google account your own
API key to use their services. Also, warning, do not use this
application in a production deployment.


First of all, first you need to **install pipenv**
* `pipenv install` (install all requirements), once loaded, don't
forget to `pipenv shell` in your terminal to activate  the environment.
The **advantage** of pipenv is that it is cross-platform. It is 
recommended by the official documentation for python's virtual
environment.

Second, run the command :
* `python -m  main` (kickstarts the server and the access to the project)
* You may connect yourself at this adress on your web browser : http://localhost:5000/ or click on
the link that is presented on in your terminal screen.
* You may now interact with Grandpy Bot, he has a bunch of positive/negative answers to reply.

### RUN Test
* Simply run this command in your terminal in the project : `pytest -vvv`


### Acknowledgment
I would like to thank my mentor, Thierry Chappuis, for all the help
and advices he gave to me to accomplish this project.