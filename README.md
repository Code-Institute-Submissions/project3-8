# FULLSTACK CRM

## Project Purpose
The purpose of this project is to deliver a website that showcases the technology we have been learning and to incorporate a form that allows customers specify a brief for a full stack development and an admin back end to reply and edit the quotes.
The 'CRM' system will be a number of forms that the customer can enter a brief for a full stack development project.
The system back end allows the comany FULLSTACK to view ,edit and respond to the project briefs recieved.
The peoject quotes  are kept in a mongo DB and can be upadted and emails sent to the customer with further information on the project.
The website is aimed at companies requiring full stack development services.

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
http://ami.responsivedesign.is/#



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
- 
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
- Quote search facility by Id, Live Date etc
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


### Testing
I tested the app as I was developing. 
I use the debugger in vscode to follow my code to look for errors.
I found that devloping some funtion first in python only and integrating with the HTML/Jinja when they were working 
helped me identify issues quicker.

- Testing implementation
- Testing write-up
- 
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:
Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Information Architecture
I have used a number of way to pass information into my website and application.
- Setting python variables
I have created a number of variable and pass them in the render template call to make it easy to customise my website.
see the nav.html where i customise the hero image and text with variables called in jinja.
- Static text
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
I installed the pep8 linter in vsode and also used an online pep8 checker.
The lines  that pass content into the pages are too long ie >80 chars for the pep8 standard.
I placed '# noqa' after these lines to tell the checker to ignore these lines.


UX wireframes


Suitability for purpose


## Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## GIT  & Version Control
[GitHub repo is here](https://github.com/ciaranq/project3)
I am using GITHB for version control and do a commit in the morning and afternoon or after major features are added.

## GIT  & Version Control
[GitHub repo is here](https://github.com/ciaranq/project3)

## Database Schema
The database schema is available in the drafts folder as a pdf file.
[Schema](https://github.com/ciaranq/project3/blob/master/drafts/CRM-schema.pdf)

## Heroku
My app has been uploaded to Heroku for deployment. I initially setup Heroku as a git remote and uploaded directly.
Auto deploy from GITHUB to heroku is now enabled.
[Heroku}](https://ciproject3-cquinlan.herokuapp.com/)


- Readme file
- Comments
- Deployment implementation
- Deployment write-up



Data handling: 
Build a mangoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. If you are considering using a different database, please discuss that with your mentor first and inform Student Care.
Database structure: Put some effort into designing a database structure well-suited for your domain. Make sure to put some thought into the nesting relationships between records of different entities.
User functionality: Create functionality for users to create, locate, display, edit and delete records (CRUD functionality).
Use of technologies: Use HTML and custom CSS for the website's front-end.
Structure: Incorporate a main navigation menu and structured layout (you might want to use Materialize or Bootstrap to accomplish this).
Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
Version control: Use Git & GitHub for version control.
Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
Make sure to not include any passwords or secret keys in the project repository.

Assessment Criteria
Your User Centric Front End Development project will be assessed based on the following criteria:

Usability and Visual Impact:
Project Purpose
UX design
Suitability for purpose
Navigation
Ease of use
Information Architecture
Defensive Design
Layout and Visual Impact:
Responsive Design
Image Presentation
Colour scheme and typography
Code Quality:
Appropriate use of HTML
Appropriate use of CSS
Appropriate use of Python
Appropriate use of the template language
Software Development practices:
Directory Structure and File Naming
Version control
Testing implementation
Testing write-up
Readme file
Comments
Data store integration
Deployment implementation
Deployment write-up
Explanation of Assessment Marks
Once you submit your milestone project, it will be reviewed by an external assessor and graded based on a particular set of criteria, specific to each module. On each criterion, the assessor will review how your project meets this criterion and award you a mark between 0 to 5:


Links for the project

## GIT  & Version Control
[GitHub repo is here](https://github.com/ciaranq/project3)

## Database Schema
The database schema is available in the drafts folder as a pdf file.
[Schema](https://github.com/ciaranq/project3/blob/master/drafts/CRM-schema.pdf)

## Heroku
My app has been uploaded to Heroku for deployment. I initially setup Heroku as a git remote and uploaded directly.
Auto deploy from GITHUB to heroku is now enabled.
[Heroku}](https://ciproject3-cquinlan.herokuapp.com/)


## Mongo
I created a database called CRM to contain my quote collection

## jobs to do
- change logo image
- connect the tech portfolio
- better validation in the form like the budget value
- add acordian to get quote
- re submit project 2
- make add status a modal
- add logo carosel https://www.solodev.com/blog/web-design/adding-an-infinite-client-logo-carousel-to-your-website.stml
- change back to false
- 


-------------------





Credits

Regna bootstrap template.

Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X