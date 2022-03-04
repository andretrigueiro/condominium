"""
Functions to operate the dababase
"""

from api.db.mongodb import DATABASE
from bson.objectid import ObjectId

"""
Converters ------------------------------------------------------------------------------------------------------
"""
# Convert all ObjectIds of residents in MongoDB to string
def convert_all_id_to_string(convert_list):
    for resident in range(len(convert_list)):
        convert_list[resident]['_id'] = str(convert_list[resident]['_id'])
    return convert_list

# Convert one ObjectId of MongoDB to string
def convert_one_id_to_string(convert_id):
    convert_id['_id'] = str(convert_id['_id'])
    return convert_id

"""
Finders ------------------------------------------------------------------------------------------------------
"""
# Get all residents in database, with IDs converted to string
def find_all_residents():
    result = list(DATABASE.residents.find())
    result = convert_all_id_to_string(result)
    return result

# Get all residents of one specific house in database
def find_residents_in_house(house_number):
    house = get_house(house_number)
    residents_of_house = house["residents"]
    return residents_of_house

# Search users in adm AND residents collections. Used within login function to define which view the page will redirect
def find_by_user(user):
    result_adm = DATABASE.adm.find_one(user)
    result_residents = DATABASE.residents.find_one(user)
    if result_adm:
        result_adm = convert_one_id_to_string(result_adm)
        return result_adm
    elif result_residents:
        result_residents = convert_one_id_to_string(result_residents)
        return result_residents
    else:
        return None

# Search resident by id
def find_resident_by_id(user_id):
    updated_id = ObjectId(user_id)
    result_residents = DATABASE.residents.find_one(updated_id)
    if result_residents:
        result_residents = convert_one_id_to_string(result_residents)
        return result_residents
    else:
        return None

"""
Getters ------------------------------------------------------------------------------------------------------
"""
# Get the user name
def get_onwer(resident_id):
    resident = find_resident_by_id(resident_id)
    resident_name = resident["name"]
    return resident_name

# Get one specific house, searched by number
def get_house(house_number):
    house = DATABASE.houses.find_one({"number": house_number})
    house = convert_one_id_to_string(house)
    return house

# Get all residents registered in database
def get_residents_options():
    residents = find_all_residents()
    final_list = []
    for resident in range(len(residents)):
        aux = {}
        aux['text'] = residents[resident]['user']
        aux['value'] = residents[resident]['user']
        final_list.append(aux)

    return final_list

# Get residents registered in one specific house
def get_residents_of_house_options(house):
    residents = find_residents_in_house(house)
    print("residents: ", residents)
    final_list = []
    for resident in range(len(residents)):
        aux = {}
        aux['text'] = residents[resident]
        aux['value'] = residents[resident]
        final_list.append(aux)

    return final_list

"""
Setters ------------------------------------------------------------------------------------------------------
"""
# Set one registered resident as onwer of a specific house
def set_onwer(house_number, resident_id):
    resident = find_resident_by_id(resident_id)
    if resident:
        selected_house = { "number": house_number }
        new_onwer = { "$set": { "onwer": resident['_id'] } }
        DATABASE.houses.update_one(selected_house, new_onwer)

# Set the price of a specific house
def set_new_price(house, new_price):
    new_price = int(new_price)

    selected_house = { "number": house }
    new_price = { "$set": { "condominium price": new_price } }

    DATABASE.houses.update_one(selected_house, new_price)
    message = "New Price Updated!"

    return message

"""
Other Functions ------------------------------------------------------------------------------------------------------
"""
# Add a new resident to database
def insert_one(resident):
    DATABASE.residents.insert_one(resident)

# Function to ADD or REMOVE residents of a specific house
def resident_to_house(action, house, resident):
    if action == "add":
        selected_house = { "number": house }
        new_resident = { "$push": { "residents": resident } }
        DATABASE.houses.update_one(selected_house, new_resident)
        message = "Resident added to house!"
        return message
    elif action == "remove":
        selected_house = { "number": house }
        remove_resident = { "$pull": { "residents": resident } }
        DATABASE.houses.update_one(selected_house, remove_resident)
        message = "Resident removed of house!"
        return message
    else:
        return "Error!"

# Function to ADD new fines to a specific house
def apply_new_fine(house, reason, price):
    price = int(price)

    new_fine = {
            'reason': reason,
            'price': price,
    }

    selected_house = { "number": house }
    fine = { "$push": { "fines": new_fine } }

    DATABASE.houses.update_one(selected_house, fine)
    message = "Fine Applied!"

    return message
