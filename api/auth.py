import functools

from flask import (
    Blueprint, g, jsonify, request, session
)
from werkzeug.security import check_password_hash, generate_password_hash

from api.db.mongodb.users_db import insert_one, find_by_user, find_all

bp = Blueprint('auth', __name__, url_prefix='/auth')

def check_user(user):
    if find_by_user(user):
            return True
    return False

@bp.route('/register', methods=('GET', 'POST'))
def register():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        email = post_data.get('email')

        if check_user(email):
            response_object['message'] = 'Email already in use! Try other'
        else:
            username = post_data.get('user')
            password = post_data.get('password')
            type = post_data.get('type')

            user_to_add = {
                'user': username,
                'password': generate_password_hash(password),
                'email': email,
                'type': type
            }
            insert_one(user_to_add)
            response_object['message'] = 'User added!'
    else:
        response_object['users'] = find_all()
    return jsonify(response_object)

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
            print("enter user")

        # elif not check_password_hash(user['password'], password):
        elif not (user['password'] == password):
            response_object['message'] = 'Incorrect password.'
            response_object['user'] = ''
            error = 'Incorrect password.'
            print("enter pass")

        if error is None:
            # print("- What is in session before clear?")
            # print(session)
            session.clear()

            session['user'] = user['user']
            session.modified = True
            # session.permanent = True

            # print("- Session new user: ", session['user'])

            # print("- What is in the final session login?")
            # print(session)

            response_object['user'] = user['user']
            response_object['type'] = user['type']
            response_object['message'] = 'User logged in!'
            # check_session()

    return jsonify(response_object)

def check_session():
    print("- Check function session")
    print(session)

@bp.before_app_request
def load_logged_in_user():
    # print("- Initial before_app_request SESSION: ")
    # print(session)
    user = session.get('user')

    if user is None:
        g.user = None
    else:
        g.user = find_by_user(user)

@bp.route('/logout')
def logout():
    session.clear()
    response_object = {'status': 'success'}
    response_object['message'] = 'User logged out!'

    return jsonify(response_object)

def login_required(view):
    response_object = {'status': 'success'}
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            response_object['message'] = 'No user logged in!'
            return jsonify(response_object)

        return view(**kwargs)

    return wrapped_view