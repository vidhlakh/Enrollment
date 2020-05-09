Flask Framework
Templates:
Make use of flask framework to develop an Enrollment Web Application
Create base templates index.html
Layout.html contains major layout such as header image
Footer.html contains footer note for all html files
nav.html is the file which has url for all other html files
courses.html has the list of courses loaded from JSON file
Register.html contains details for registering the user
Login.html contains login details for the user

forms.py make use of Flask WTF and implements Login form, Register form
Add Validators such as Required field, maximum length, using WTforms.validators
Do Password Hashing and unhashing
Make use of Session to handle user_ID

Routes.py has the methods specific to the url.

Connect to the MongoDB using Mongo Engine
USe Aggregation Pipeline to aggregate Course and USer database into Enrollemnt Database 
