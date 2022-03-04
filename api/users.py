"""
Users related functions.
In this project, the users are admin or residents.
Dates used in this project are strings hard coded and didnt use some date format because I didnt have time to adapt it.
"""

from api.db.mongodb.users_db import insert_one, get_residents_options, resident_to_house, get_residents_of_house_options

from flask import (
    Blueprint, jsonify, request
)

bp = Blueprint('users', __name__, url_prefix='/users')

# Function to return all residents of database in OPTION format to be used at select button
@bp.route('/all_residents_options', methods=('GET', 'POST'))
def all_residents_options():
    response_object = {'status': 'success'}

    residents = get_residents_options()
    response_object['residents'] = residents

    return jsonify(response_object)

# Function to return all residents of specific house in OPTION format to be used at select button
@bp.route('/residents_of_house_options', methods=('GET', 'POST'))
def residents_of_house_options():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        house = post_data.get('house')
        if house:
            residents = get_residents_of_house_options(house)
            print("residents: ", residents)
            response_object['residents'] = residents

    return jsonify(response_object)

# Add a new resident to database. The default user is the name + ".cond" and the initial password is the birthdate
@bp.route('/set_new_resident', methods=('GET', 'POST'))
def set_new_resident():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        name = post_data.get('name')
        email = post_data.get('email')
        day = post_data.get('day')
        month = post_data.get('month')
        year = post_data.get('year')
        house_number = post_data.get('house_number')

        user = (name.lower() + '.cond')

        birthdate = day + '/' + month + '/' + year
        password = birthdate

        type = 'resident'

        newResident = {
            'user': user,
            'password': password,
            'name': name,
            'email': email,
            'type': type,
            'birthdate': birthdate,
            'house': house_number
        }

        insert_one(newResident)
        message = resident_to_house("add", house_number, newResident['user'])

        response_object['user'] = user
        response_object['password'] = password
        response_object['message'] = 'Resident added!'

    return jsonify(response_object)

# Add a new resident to specific house.
@bp.route('/add_new_resident', methods=('GET', 'POST'))
def add_new_resident():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        house = post_data.get('house')
        resident = post_data.get('resident')

        message = resident_to_house('add', house, resident)
        response_object['message'] = message

    return jsonify(response_object)

# Remove a registered resident of specific house.
@bp.route('/remove_resident_house', methods=('GET', 'POST'))
def remove_resident_house():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        house = post_data.get('house')
        resident = post_data.get('resident')

        message = resident_to_house('remove', house, resident)
        response_object['message'] = message

    return jsonify(response_object)

