# Condominium
This project is a manager of condominiums fees.
It's a study project using Flask + VueJs + MongoDB.

# How to install the project

### Dependencies that you need to install
Frontend (can install with npm):
- Vue v2.6.11
- Vue CLI v4.5.11
- Bootstrap-vue v2.21.2
- Vue-cookies v1.7.4
- Axios v0.21.1

Backend:
- Python v3.10
- Flask v2.0.1
- Flask-Cors v3.0.10
- Flask-Session latest version
- pymongo latest version
- pymongo[aws] latest version
- dnspython latest version

### Installing
Install the frontend dependencies with npm. To configure Vue CLI, you can copy the configuration of this tutorial:
> https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

If you already have python installed, install the virtual enviroment. Acess the api directory and run these commands:
> $ python3.9 -m venv env

> $ source env/bin/activate

After that, use the pip tool to install the requirements. Run this command on terminal:
> (env)$ pip install -r api/requirements/requirements.txt

### Database config
I used a .env file to store the MongoDB connection. If you want to do the same, install dotenv package with pip and set the variables in "/api/db/mongodb/init.py"

# How to run the project
You will need 2 different terminals to run the application.

Note: The DATABASE does not come configured. You neet to set the variable to make the connection with your Mongo.

### Backend
Open a new terminal. Acess the project folder and activate the env:

> $ source env/bin/activate

The virtual environment should turn on and the terminal will be like this:

> (env)$

Then, set the environment:

> (env)$ export FLASK_APP=api

> (env)$ export FLASK_ENV=development

After that, run the application:

> (env)$ flask run

To test if the app is working fine, point your browser at http://localhost:5000/ping. You should see:

> "pong!"

### Populate the database
If you want to populate the database with test data, open a new terminal, activate and set the parameters of environment and run this command:

> (env)$ flask populate-db

After that, you can close the terminal.

Note: Remember to set the DATABASE connection.

### Frontend

Open a new terminal. In the client folder of the project, activate vue:

> $ npm run serve

To test if the app is working fine, point your browser at http://localhost:8080. You should see:

![](/client/public/homepage.png)

# How to use the project
Note: Right now, the House Card doesn't update some stats automatically.
If you make some change, just select other house and come back to the house that you made the changes.

In the homepage, press the login button and enter the user.

For adm permissions:
- user: syndicate.cond
- password: 123

For resident permissions:
- user: maria.cond
- password: 12345

Adm user can:
- Register new residents.
- Add residents to houses.
- Remove residents of houses.
- Set condominium values.
- Fine residents for some reason.

Resident user can:


# Known issues and Improviments
The project is very basic, so it doenst have security focus. Some acess functions and comparisons are very limited and simple.

#### Backend
Auth:
- Put the Session tool to work. After that:
- Session - before_app_request
- Session - logout
- Session - login required

#### Frontend
Big issue:
- If the user press F5, the cookie is reseted. Need to use some solution as vuex to double store the user logged.
- The cookie issue is related to permisions of user logged in.

Login:
- Check if some user is logged in to log automatically

Header:
- Put the other nav-itens

House card:
- Update the card to modify the content automatically. Couldn't resolve this in time
- Organize better the data displayed
- Maybe change the Card component to table

