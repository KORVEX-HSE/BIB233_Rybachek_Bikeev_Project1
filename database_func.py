from aiogram.types import Message, CallbackQuery
from SQL_class import *



users = Table('users', ['id', 'first_name', 'username'])
parameters = Table('parameters', ['user_id', 'age', 'hight', 'weight', 'life_style', 'mission'])
status = Table('status', ['datas', 'user_id', 'st_prot', 'st_fat', 'st_carb', 'st_cal'])



def check_user_list_message(message: Message):
    if message.from_user.id not in users.show_id():
        users.new_str(f'{message.from_user.id}', [f'{message.from_user.first_name}', f'{message.from_user.username}', 'not_day'])
    return True



def check_parameter_list_query(callback: CallbackQuery):
    if callback.from_user.id not in parameters.show_id():
        parameters.new_str(f'{callback.from_user.id}', ['-1', '-1', '-1', 'e', 'e', 'e'])
    #else:
        #parameters.change_full_str(f'{callback.from_user.id}', ['-1', '-1', '-1', 'e', 'e', 'e'])
    return True



def check_stat(datas, user_id):
    res = list()

    st_prot = status.show_special_status(datas, user_id, 'st_prot')
    res.append(st_prot)

    st_fat = status.show_special_status(datas, user_id, 'st_fat')
    res.append(st_fat)

    st_carb = status.show_special_status(datas, user_id, 'st_carb')
    res.append(st_carb)

    st_cal = status.show_special_status(datas, user_id, 'st_cal')
    res.append(st_cal)

    return res