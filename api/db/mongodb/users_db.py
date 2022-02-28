from api.db.mongodb import DATABASE

def convert_all_id_to_string(convert_list):
    for resident in range(len(convert_list)):
        convert_list[resident]['_id'] = str(convert_list[resident]['_id'])
    return convert_list

def convert_one_id_to_string(convert_id):
    convert_id['_id'] = str(convert_id['_id'])
    return convert_id

def find_all():
    result = list(DATABASE.residents.find())
    result = convert_all_id_to_string(result)
    return result

def find_by_user_id(id):
    result = DATABASE.users.find_one(id)
    if result:
        result = convert_one_id_to_string(result)
    return result

def find_one(user_id):
    result = DATABASE.users.find_one({'_id': user_id})
    return result

def insert_one(resident):
    DATABASE.residents.insert_one(resident)