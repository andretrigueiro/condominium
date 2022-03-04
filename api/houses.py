"""
Houses related functions.
In this project, the condominium properties are being treated as houses.
"""

from api.db.mongodb.users_db import get_onwer, get_house, set_new_price, apply_new_fine

from flask import (
    Blueprint, jsonify, request
)

bp = Blueprint('houses', __name__, url_prefix='/houses')

# Function to return the data of a especific house requested by client
@bp.route('/select_house', methods=('GET', 'POST'))
def select_house():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        house_number = post_data.get('houseNumber')

        house = get_house(house_number)

        if house:
            response_object['number'] = house['number']
            response_object['onwer'] = get_onwer(house['onwer'])
            response_object['residents'] = house['residents']
            response_object['condominiumP'] = house['condominium price']
            response_object['debts'] = house['debts']
            response_object['payments'] = house['payments']
            response_object['fines'] = house['fines']
            response_object['message'] = 'House Informed!'

    return jsonify(response_object)

# Function to set a new condominium price to specific house
@bp.route('/set_price', methods=('GET', 'POST'))
def set_price():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        house_number = post_data.get('house')
        new_price = post_data.get('price')

        message = set_new_price(house_number, new_price)

        response_object['message'] = message

    return jsonify(response_object)

# Function to add new fines to specific house
@bp.route('/apply_fine', methods=('GET', 'POST'))
def apply_fine():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()

        house_number = post_data.get('house')
        reason = post_data.get('reason')
        price = post_data.get('price')

        message = apply_new_fine(house_number, reason, price)

        response_object['message'] = message

    return jsonify(response_object)