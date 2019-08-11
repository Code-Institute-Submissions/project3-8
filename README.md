# FULLSTACK CRM

## Project Purpose
The purpose of this project is to deliver a website that showcases the technology we have been learning and to incorporate a form that allows customers specify a brief for a full stack development.
The site has an admin back end to reply and edit the quotes.
The 'CRM' system will be a number of forms that the customer can enter a brief for a full stack development project.
The system back end allows the company FULLSTACK to view ,edit and respond to the project briefs recieved.
The peoject quotes are kept in a mongo DB and can be upadted and emails sent to the customer with further information on the project.
The website is aimed at companies requiring full stack development services.
The portfolio feature lists a number of full stack tech and further information is available by selecting a card.


##  UX - User Experience

### User stories
I want user to be informed about full stack development and to request a quote for a full stack project. 
I envisage a customer looking for full stack project providers to visit the site and get all the information they need.
The customer can use the New quote form to complete  a project brief that can be responded to by Full stack.

As a user type, I want to learn more about full stack development and make contact with FULLSTACK to start a conversation.
Seee the links below for data schema etc.

### Navigation
The navigation is based on a top bootstrap menu with some further menues in the quote pages.
I plan to use pills in the page that displays the quotes

### UX design
I modified a bootstrap template that I am fanmiliar with for information pages and designed all the forms with bootsrap.
I wanted to use different input types to collect the information on the forms.

### Responsive Design
I have used bootsrap throughout the project. The page elements look well on screens as small as 360 pixels wide and as big as 3840 pixels wide (4K).	Bootstrap grid sizes and CSS3 media queries  are used to ensure the layout changes appropriately and reflows when the screen is resized.
[Responsive test](http://ami.responsivedesign.is/?url=https%3A%2F%2Fciproject3-cquinlan.herokuapp.com)


## Database Schema
The database schema is available in the drafts folder as a pdf file.
[Schema](https://github.com/ciaranq/project3/blob/master/drafts/CRM-schema.pdf)


## Features
### Home page /
  - about us , facts, call to action to request quote, contact page.
  - Portfolio page 
  - Request New quote page
  - Quote Admin menu
- 
### Database connected  Features
- Contact page that replies with email and stores the contact in the database.
- All contact request are stored with status of NEW
- New Quote link calls form and contents are stored in database and given unique quote Id
* Customer Functions in app.py
  - New Quote: add a new quote for a customer and assigns it a status of NEW
    - Generates a unique Quote Id by adding 1 to the Quote id stored in the  quotenumber document.
    - Displays a page showing success and the quote number that has been generated
    - Email the new quote  to customer in place but not connected
  - View Quote: This allows the customer to view his quote based on their unique Quote ID
  - Customer contact page: the data entered on the contact page on the home page is stored in the Database.
    - The customer page send an email to the customer with the email.js api.

* Admin Functions in app.py
  - GET Quotes: list all quotes and sorts them in decending order
    - admin user can select to view quotes by status
    - links to edit and delete quotes.
  - Edit Quote: allows admin user to edit the quote and add the information to reply to the quote
    - allows admin to change the status os the quote
  - Delete quote: deletes the quotes

- Quote Admin menu  - View and Edit Quotes in the database, (full CRUD fetures)
                    - Manage Quote Status (full CRUD features)

### Static JSON file driven Features
- Portfolio page, connected to static json fil
I am using a static JSON file in my data directory to drive my portfolio pages.
I will put this in a mongodb later , it was just quicker to import everyting from a json file 
  - Portfolio page list all the Full stack portfolio we work on and these are taken from the JSON file.
  - The filter tabs are driven form the JSON file and are  used to call css classes for display.
  - Each card then calls a member route and loads the description etc. form the JSOM.
  - This can be easily converted to a DB as all the json work has been done
- 
.
### Future Features.
- DB driven portfolio pages
- Quote search facility by tech type, Live Date etc
- 

## Technologies Used
The quote application is built with Python, Flask, Html and Jinja.
The Database used is Mongo DB
Frameworks:
    Flask
    Vootstrap
Libraries:
    JavaScriptJQuery - email sending
    Bootstrap - template
    Font Awesome - used in the template for icons etc
    Animate - template animation
    Flask - os, render template, import os, redirect, request, url_for, PyMongo, ObjectId
    Tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

    For a full list of what i used selet this built with link
[Built with](https://builtwith.com/?https%3a%2f%2fciproject3-cquinlan.herokuapp.com%2f)


### Testing
I tested the app as I was developing. 
I use the debugger in vscode to follow my code to look for errors.
I found that devloping some funtion first in python only and integrating with the HTML/Jinja when they were working 
helped me identify issues quicker.


### Information Architecture
I have used a number of ways to pass information into my website and application.
- Setting python variables
I have created a number of variable and pass them in the render template call to make it easy to customise my website.
see the nav.html where i customise the hero image and text with variables called in jinja.
- Static json text
I created a static json text file and this drives the tech portfolio pages
- Mongo Database
The Quote and contact page information is stored in a Mongo database
The data schema is located at https://github.com/ciaranq/project3/blob/master/static/CRM-schema.pdf

### Directory Structure and File Naming
- The python file to run the flask app is in the root.
- Static directory contains the following
  - CSS : Main css file with my modifications
  - Javascript : Main js file with the sendmail and sendquote scripts.
  - img : Image files
  - lib : Contains downloaded libraries for the temmplate and bootstrap

#### PEP8
I installed the pep8 linter in vscode and also used an online pep8 checker.
The lines that pass content into the pages are too long ie >80 chars for the pep8 standard.
I placed '# noqa' after these lines to tell the checker to ignore these lines.


## Deployment

## Heroku
The project and my app has been uploaded to Heroku for deployment. I initially setup Heroku as a git remote and uploaded directly.
Auto deploy from GITHUB to heroku is now enabled.
[Heroku}](https://ciproject3-cquinlan.herokuapp.com/)

## GIT  & Version Control
[GitHub repo is here](https://github.com/ciaranq/project3)
I am using GITHB for version control and do a commit in the morning and afternoon or after major features are added.




## Links for the project

## GIT  & Version Control
[GitHub repo is here](https://github.com/ciaranq/project3)

## Database Schema
The database schema is available in the drafts folder as a pdf file.
[Schema](https://github.com/ciaranq/project3/blob/master/drafts/CRM-schema.pdf)

## Heroku
My app has been uploaded to Heroku for deployment. I initially setup Heroku as a git remote and uploaded directly.
Auto deploy from GITHUB to heroku is now enabled.
[Heroku](https://ciproject3-cquinlan.herokuapp.com/)

## Mongo
I created a database called CRM to contain my quote collection








### Credits

Regna bootstrap template.
Portfolio Content: The text for section was copied from the Wikipedia articles
Portfolio Images: The photos used in this site were obtained from the relevant pages for the technology

Fonts: 
Google Font API
Font Awesome
Iconic font and CSS toolkit.


Frameworks:
Python: Python 3.6
Heroku 
Flask


Content Delivery Network
View Global Trends
AJAX Libraries APIAJAX Libraries API
AJAX Libraries API Usage Statistics · Download List of All Websites using AJAX Libraries API

The AJAX Libraries API is a content distribution network and loading architecture for the most popular, open source JavaScript libraries.

jQuery: JQuery is a fast, concise, JavaScript Library that simplifies how you traverse HTML documents, handle events, perform animations, and add Ajax interactions to your web pages. jQuery is designed to change the way that you write JavaScript.

JavaScript Library
WOW: Reveal CSS animation as you scroll down a page.
jQuery Waypoints : Waypoints is a small jQuery plugin that makes it easy to execute a function whenever you scroll to an element.
Hover Intent: hoverIntent is a plug-in that attempts to determine the user's intent. 


UTF-8 (8-bit UCS/Unicode Transformation Format) is a variable-length character encoding for Unicode. It is the preferred encoding for web pages.

CSS
Twitter Bootstrap: Bootstrap is a toolkit from Twitter designed to kickstart development of webapps and sites.
