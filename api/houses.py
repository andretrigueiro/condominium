from api.db.mongodb.users_db import insert_one, find_by_user, find_all_residents, get_onwer, get_house

from flask import (
    Blueprint, flash, g, jsonify, request, session
)

bp = Blueprint('houses', __name__, url_prefix='/houses')

@bp.route('/select_house', methods=('GET', 'POST'))
def select_house():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        house_number = post_data.get('houseNumber')

        print("house number: ", house_number)

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
