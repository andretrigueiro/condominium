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

def insert_one(resident):
    DATABASE.residents.insert_one(resident)