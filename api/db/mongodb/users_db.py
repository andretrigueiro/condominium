from api.db.mongodb import DATABASE
from bson.objectid import ObjectId

def convert_all_id_to_string(convert_list):
    for resident in range(len(convert_list)):
        convert_list[resident]['_id'] = str(convert_list[resident]['_id'])
    return convert_list

def convert_one_id_to_string(convert_id):
    convert_id['_id'] = str(convert_id['_id'])
    return convert_id

def find_all_residents():
    result = list(DATABASE.residents.find())
    result = convert_all_id_to_string(result)
    return result

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

def find_resident_by_id(user_id):
    print("Type user: ", type(user_id))
    updated_id = ObjectId(user_id)
    print("Type updated: ", type(updated_id))
    result_residents = DATABASE.residents.find_one(updated_id)
    if result_residents:
        result_residents = convert_one_id_to_string(result_residents)
        return result_residents
    else:
        return None

def insert_one(resident):
    DATABASE.residents.insert_one(resident)

def set_onwer(house_number, resident_id):
    resident = find_resident_by_id(resident_id)
    if resident:
        selected_house = { "number": house_number }
        new_onwer = { "$set": { "onwer": resident['_id'] } }
        DATABASE.houses.update_one(selected_house, new_onwer)

def get_onwer(resident_id):
    resident = find_resident_by_id(resident_id)
    resident_name = resident["name"]
    return resident_name

def get_house(house_number):
    house = DATABASE.houses.find_one({"number": house_number})
    print("house: ", house)
    house = convert_one_id_to_string(house)
    return house

def get_residents_options():
    residents = find_all_residents()
    final_list = []
    for resident in range(len(residents)):
        aux = {}
        aux['text'] = residents[resident]['user']
        aux['value'] = residents[resident]['user']
        final_list.append(aux)

    return final_list

def resident_to_house(action, house, resident):
    if action == "add":
        selected_house = { "number": house }
        new_resident = { "$push": { "residents": resident } }
        DATABASE.houses.update_one(selected_house, new_resident)
        return True
    else:
        return False