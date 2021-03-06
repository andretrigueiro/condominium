"""
Authentication functions.
Login function define the view of frontend user.
Tried to implement the Session tool to double check the security between requests, however I had some problems and couldnt finish it in time.
So, only the Login route works right now.
"""

import functools

from flask import (
    Blueprint, g, jsonify, request, session
)
from werkzeug.security import check_password_hash, generate_password_hash

from api.db.mongodb.users_db import find_by_user, set_new_password

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Login function. Check the user in backend and define the type of acess it will has
@bp.route('/login', methods=('GET', 'POST'))
def login():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        user_login = post_data.get('user')
        password = post_data.get('password')
        error = None

        user = find_by_user({"user": user_login})

        if user is None:
            response_object['message'] = 'Couldnt find user.'
            response_object['user'] = ''
            error = 'Couldnt find user.'

        # elif not check_password_hash(user['password'], password):
        elif not (user['password'] == password):
            response_object['message'] = 'Incorrect password.'
            response_object['user'] = ''
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user'] = user['user']
            session.modified = True

            response_object['user'] = user['user']
            response_object['first_login'] = user['first_login']
            response_object['type'] = user['type']
            if user['type'] == 'resident':
                response_object['house_number'] = user['house']
            response_object['message'] = 'User logged in!'

    return jsonify(response_object)

# Change the user password
@bp.route('/change_password', methods=('GET', 'POST'))
def change_password():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        user_login = post_data.get('user')
        new_password = post_data.get('password')
        error = None

        user = find_by_user({"user": user_login})
        set_new_password(user['_id'], new_password)

        if user is None:
            response_object['message'] = 'Couldnt find user.'
            response_object['user'] = ''
            error = 'Couldnt find user.'

        if error is None:
            response_object['message'] = 'Password changed!'

    return jsonify(response_object)

# Function called before each request to check if the user is logged. Used for security
@bp.before_app_request
def load_logged_in_user():
    user = session.get('user')

    if user is None:
        g.user = None
    else:
        g.user = find_by_user(user)

# Logout function. It should clear the session user if it was working. However, rightnow, just return a message.
@bp.route('/logout')
def logout():
    session.clear()
    response_object = {'status': 'success'}
    response_object['message'] = 'User logged out!'

    return jsonify(response_object)

# Function to check if a user is already logged.
def login_required(view):
    response_object = {'status': 'success'}
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            response_object['message'] = 'No user logged in!'
            return jsonify(response_object)

        return view(**kwargs)

    return wrapped_view