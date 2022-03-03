from api.db.mongodb.users_db import insert_one, get_residents_options, resident_to_house

from flask import (
    Blueprint, flash, g, jsonify, request, session
)

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/all_residents', methods=('GET', 'POST'))
def all_residents():
    response_object = {'status': 'success'}

    residents = get_residents_options()
    response_object['residents'] = residents

    return jsonify(response_object)

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
            'birthdate': birthdate
        }

        insert_one(newResident)

        response_object['user'] = user
        response_object['password'] = password
        response_object['message'] = 'Resident added!'

    return jsonify(response_object)

@bp.route('/add_new_resident', methods=('GET', 'POST'))
def add_new_resident():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        house = post_data.get('house')
        resident = post_data.get('resident')

        resident_to_house('add', house, resident)
        response_object['message'] = 'Resident added to house!'

    return jsonify(response_object)