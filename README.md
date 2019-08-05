# README.md
This is the start of my project.
I have done some bits already as I was doing test tasks while I was followingthe videos and doing the mini projects.
Some git commits will be quick as a result.



## jobs to do
- change logo image
- heroku setup working

- set function
- new quote
- format forms
- add acordian to get quote
- re submit project 2
- make add status a modal
- add logo carosel https://www.solodev.com/blog/web-design/adding-an-infinite-client-logo-carousel-to-your-website.stml
- change back to false
- 



### Testing
I tested the app as I was developing. 
I use the debugger in vscode to follow my code to look for errors.
I found that devloping some funtion first in python only and integrating with the HTML/Jinja when they were working 
helped me identify issues quicker.


#### PEP8
I installed the pep8 linter in vsode and also used an online pep8 checker.
The lines  that pass content into the pages are too long ie >80 chars for the pep8 standard.
I placed '# noqa' after these lines to tell the checker to ignore these lines.




ux wireframes




# Project Purpose
The purpose of this project is to deliver a website that showcases the technology we have been learning and to incorporate a form that allows customers specify a brief for a full stack development and an admin back end to reply and edit the quotes.
The 'CRM' system will be a number of forms that the customer can enter a brief for a full stack development project.
The system will also have a back end to view ,edit and respond to the project briefs recieved.

User stories
i want user to be able to request a quote for a full stack project. 
I envisage a customer looking for full stack project providers to visit the site and get all the information they need.
The customer can use the New quote form to complete  a project brief that can be responded to by Full stack.

UX design
I have used a template that I am fanmiliar with for some pages and designed the forms with the aim of using different input types to collect the information.


- Suitability for purpose



- Navigation

the navigation is based on a top bootstrap menu with some further menues in the quote pages.
 I plan to use pills in the page that displays the quotes

- Ease of Use
- 
- Information Architecture
I have used a number of way to pass information into my website and application.
# Setting python variables
I have created a number of variable and pass them in the render template call to make it easy to customise my website.
see the nav.html where i customise the hero image and text with variables called in jinja.
#Static text
I created a static json text file and this drives the tech portfolio pages
#Mongo Database
The Quote and contact page information is stored in a Mongo database
The data schema is located in  



- Responsive Design
- Image Presentation
- Colour scheme and typography
- Appropriate use of HTML
- Appropriate use of CSS
- Directory Structure and File Naming
- Version Control
I am using GITHB for version control and do a commit in the morning and afternoon or after major features are added.


- Testing implementation
- Testing write-up
- Readme file
- Comments
- Deployment implementation
- Deployment write-up


Mandatory Requirements
A project violating any of these requirements will FAIL

Data handling: Build a mangoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. If you are considering using a different database, please discuss that with your mentor first and inform Student Care.
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

0 marks - Entirely missing
The requirements for this criterion were completely ignored
1 mark - Non Functioning
The criterion is only partially implemented and remains essentially non functioning
2 marks - Fails to Meet Expectations
The criterion is mostly satisfied but has significant technical issues or other flaws
3 marks - Meets Expectations
The criterion is fully satisfied without any significant issues, but is otherwise simple and doesn’t demonstrate any striving for excellence
4 marks - Exceeds Expectations
The criterion is satisfied in a fully professional manner and demonstrating that the student strived for excellence, even if there are perhaps 1 or 2 minor issues.
5 marks - Greatly Exceeds Expectations
The criterion was implemented flawlessly, exhibiting a well-planned approach and excellent execution; this project should be showcased for other students to learn from.



## GIT 
[GitHub repo is here](https://github.com/ciaranq/project3)

## Database Schema
The database schema is available in the drafts folder as a pdf file.
[Schema](https://github.com/ciaranq/project3/blob/master/drafts/CRM-schema.pdf)

## Heroku
My app can be found at https://ciproject3-cquinlan.herokuapp.com/
auto deploy from GITHUB to heroku is enabled

## Mongo
I created a database called CRM to contain my quote collection

