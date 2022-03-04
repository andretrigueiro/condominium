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
- Install the frontend dependencies with npm. To configure Vue CLI, you can use the configuration of this tutorial:
> https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

- If you already have python installed, install the virtual enviroment. Acess the api directory and run this command::
> python3.9 -m venv env
> source env/bin/activate

After that, use the pip tool to install the requirements. Run this command on terminal:
> pip install -r api/requirements/requirements.txt

# How to run the project
You will need 2 different terminals to run the application.

The DATABASE does not come configured. You neet to set a .env with the DATABASE information.

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

### Vue section

Open a new terminal. In the client folder of the project, activate vue:

> $ npm run serve

To test if the app is working fine, point your browser at http://localhost:8080. You should see:

![](/client/public/homepage.png)

