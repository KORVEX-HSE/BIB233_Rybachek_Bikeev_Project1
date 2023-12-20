from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, FSInputFile, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from datetime import date
import os

from SQL_class import *
from calculators_funk import *
from database_func import *
from keyboards import *
from grafics import *



BOT_TOKEN = '6931786652:AAESChx4LZ67NXsoohxC8kDzjgIJd-PBMEk'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

users = Table('users', ['id', 'first_name', 'username', 'situation'])
parameters = Table('parameters', ['user_id', 'age', 'hight', 'weight', 'life_style', 'mission'])
foods = Table('foods', ['food_name', 'food_group', 'food_calorie', 'food_protein', 'food_fat', 'food_carbon'])
opera_food_users = Table('opera_food_users', ['user_id','opera_food_name', 'opera_food_type'])
opera_vals_users = Table('opera_vals_users', ['user_id', 'opera_prot', 'opera_fat', 'opera_carb', 'opera_cal'])




class FSMFillForm(StatesGroup):

    day = State()
    not_day = State()
    go_rec = State()
    go_gen = State()
    go_ahw = State()
    go_style = State()
    go_goal = State()
    go_graph_r = State()
    go_fix = State()
    go_groups = State()
    go_dop = State()
    go_new = State()
    go_append = State()
    go_after_append = State()
    go_dop_f = State()
    go_after_dop_f = State()
    go_pre_graph_f = State()
    go_graph_f = State()
    statist = State()
    go_input = State()
    go_datas = State()



# BLOCK start
@dp.message(CommandStart(), StateFilter(default_state))
async def process_start_command_mess(message: Message, state: FSMContext):
    if check_user_list_message(message):
        await state.set_state(FSMFillForm.not_day)
        #users.change_one_str(f'{message.from_user.id}', 'situation', 'not_day')
        await message.answer(f'Привет, {message.from_user.first_name}.')
        await message.answer(
            text='Выберите опцию:',
            reply_markup=keyboard_start)



@dp.message(StateFilter(default_state))
async def process_start_command_call(message: Message, state: FSMContext):
    await state.set_state(FSMFillForm.not_day)
    await message.answer(
        #chat_id=f'{callback.from_user.id}',
        text='Выберите опцию:',
        reply_markup=keyboard_start)
    


# BLOCK pfc
@dp.callback_query(StateFilter(FSMFillForm.not_day), F.data == 'new_day')
async def norm_pfc(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.day)
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'day')
    if check_parameter_list_query(callback):
        await callback.message.edit_text(
            #chat_id=f'{callback.from_user.id}', 
            text='Нажмите на кнопку:',
            reply_markup = keyboard_PFC)
    await callback.answer()



# BLOCK qender
@dp.callback_query(F.data =='PFC', StateFilter(FSMFillForm.day))
async def gender_user(callback: CallbackQuery, state: FSMContext):
        await state.set_state(FSMFillForm.go_rec)
        #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_rec')
        await callback.message.edit_text(
            #chat_id=f'{callback.from_user.id}',
            text='Выберите ваш пол:',
            reply_markup=keyboard_qender)
        await callback.answer()



# OVAL ahw
@dp.callback_query(F.data == 'man', StateFilter(FSMFillForm.go_rec))
@dp.callback_query(F.data == 'woman', StateFilter(FSMFillForm.go_rec))
async def ahw_user(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.go_gen)
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_qen')
    parameters.change_one_str(f'{callback.from_user.id}', 'gender', f'{callback.data}')
    await callback.message.edit_text(#chat_id=f'{callback.from_user.id}', 
                            text='Введите через пробел: ваш возраст(полных лет), ваш рост(в сантиметрах), ваш вес(в килограммах)')
    await callback.answer()



# BLOCK style
@dp.message(StateFilter(FSMFillForm.go_gen))
async def style_life(message: Message, state: FSMContext):
    await state.set_state(FSMFillForm.go_ahw)
    #users.change_one_str(f'{message.from_user.id}', 'situation', 'go_ahw')
    ahw_list: str = message.text.split()
    parameters.change_one_str(f'{message.from_user.id}', 'age', f'{ahw_list[0]}')
    parameters.change_one_str(f'{message.from_user.id}', 'hight', f'{ahw_list[1]}')
    parameters.change_one_str(f'{message.from_user.id}', 'weight', f'{ahw_list[2]}')
    await bot.send_message(
        chat_id=f'{message.from_user.id}',
        text='Выберите ваш уровень активности:',
        reply_markup=keyboard_style)



# BLOCK goal
@dp.callback_query(F.data =='very_low', StateFilter(FSMFillForm.go_ahw))
@dp.callback_query(F.data =='low', StateFilter(FSMFillForm.go_ahw))
@dp.callback_query(F.data =='middle', StateFilter(FSMFillForm.go_ahw))
@dp.callback_query(F.data =='hard', StateFilter(FSMFillForm.go_ahw))
async def goal(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.go_style)
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_style')
    parameters.change_one_str(f'{callback.from_user.id}', 'life_style', f'{callback.data}')
    await callback.message.edit_text(
        #chat_id=f'{callback.from_user.id}',
        text='Выберите вашу цель:',
        reply_markup=keyboard_goal)
    await callback.answer()



# RHOMBUS graph_r
@dp.callback_query(F.data =='gain', StateFilter(FSMFillForm.go_style))
@dp.callback_query(F.data =='balance', StateFilter(FSMFillForm.go_style))
@dp.callback_query(F.data =='loss', StateFilter(FSMFillForm.go_style))
@dp.callback_query(F.data == 'recom', StateFilter(FSMFillForm.go_style))
async def call_recomendation(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.go_goal)
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_goal')
    parameters.change_one_str(f'{callback.from_user.id}', 'mission', f'{callback.data}')
    w = (parameters.show_str([f'{callback.from_user.id}'])[0])[1:7]
    a, b, c, d, e, f = w[0], w[1], w[2], w[3], w[4], w[5]
    vals_r = calculate_macros(a, b, c, d, e, f) 
    data = str(date.today()).split('-')
    graph_r = recomend_graph(callback.from_user.id, callback.from_user.first_name, data, vals_r)
    await callback.message.answer_photo(graph_r, caption=f'За день следует употребить <b>{vals_r[-1]}</b> килокалорий\n\nНапиши любую букву для перехода на следующий шаг', parse_mode='HTML')
    os.remove(f"graphs/graph_r{callback.from_user.id}.png")
    opera_vals_users.new_str(f'{callback.from_user.id}', ['0', '0', '0', '0'])
    await callback.answer()



# qwerty
@dp.message(StateFilter(FSMFillForm.go_goal, FSMFillForm.go_after_dop_f, FSMFillForm.go_after_append))
async def call(message: Message, state: FSMContext):
    await state.set_state(FSMFillForm.go_graph_r)
    #opera_food_users.new_str(f'{message.from_user.id}', ['WAIT', 'WAIT'])
    await bot.send_message(
        chat_id=f'{message.from_user.id}',
        text='Выберите действие:',
        reply_markup = keyboard_fixation)



# BLOCK fixation -> go_fix
@dp.callback_query(F.data == 'fix', StateFilter(FSMFillForm.go_graph_r))
async def fixat(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.go_fix)
    opera_food_users.new_str(f'{callback.from_user.id}', ['WAIT', 'WAIT'])
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_fix')
    await bot.send_message(
        chat_id=f'{callback.from_user.id}',
        text='Выберите группу продуктов:',
        reply_markup = keyboard_groups)
    await callback.answer()


 
# OVAL type_name
@dp.callback_query(F.data == 'sweet', StateFilter(FSMFillForm.go_fix))
@dp.callback_query(F.data == 'fat_group', StateFilter(FSMFillForm.go_fix))
@dp.callback_query(F.data == 'animal', StateFilter(FSMFillForm.go_fix))
@dp.callback_query(F.data == 'group', StateFilter(FSMFillForm.go_fix))
@dp.callback_query(F.data == 'green', StateFilter(FSMFillForm.go_fix))
@dp.callback_query(F.data == 'no_sug_drink', StateFilter(FSMFillForm.go_fix))
async def type_name(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.go_groups)
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_groups')
    opera_food_users.change_one_str(f'{callback.from_user.id}', 'opera_food_type', f'{callback.data}')
    await callback.message.edit_text(#chat_id=f'{callback.from_user.id}', 
                            text='Введите наименование продукта:')
    await callback.answer()



# BLOCK append
@dp.message(StateFilter(FSMFillForm.go_groups))
async def app_food(message: Message, state: FSMContext):
    opera_food_users.change_one_str(f'{message.from_user.id}', 'opera_food_name', f'{message.text.lower()}')
    if message.text.lower() in foods.show_id():
        await state.set_state(FSMFillForm.go_dop)
        #users.change_one_str(f'{message.from_user.id}', 'situation', 'go_dop')
        #opera_food_users.del_str(f'{message.from_user.id}')
        await bot.send_message(chat_id=f'{message.from_user.id}', 
                                text='Продукт есть в базе\nНапиши любую букву, чтобы продолжить')
    elif message.text.lower() not in foods.show_id():
        await state.set_state(FSMFillForm.go_new)
        #users.change_one_str(f'{message.from_user.id}', 'situation', 'go_new')
        await bot.send_message(chat_id=f'{message.from_user.id}', 
                                text='Нажми на кнопку', 
                                reply_markup=keyboard_append)



@dp.message(StateFilter(FSMFillForm.go_dop))
async def type_not_full(message: Message, state: FSMContext):
    await state.set_state(FSMFillForm.go_dop_f)
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_append')
    await bot.send_message(
        chat_id=f'{message.from_user.id}',
        text='Введите количество (в граммах) съеденного продукта, указанного вами ранее\n\n<i>Пример правильного ввода: 350</i>', parse_mode='HTML')



@dp.callback_query(F.data == 'append', StateFilter(FSMFillForm.go_new))
async def type_full(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.go_append)
    #users.change_one_str(f'{callback.from_user.id}', 'situation', 'go_append')
    await bot.send_message(
        chat_id=f'{callback.from_user.id}',
        text='Введите через пробел значения количества белков, жиров и углеводов в граммах и количество Ккал на 100 грамм и вес в граммах съеденного продукта\n\n<i>Пример правильного ввода:  23 56 32 197 350</i>', parse_mode='HTML')
    await callback.answer()



@dp.message(StateFilter(FSMFillForm.go_dop_f))
async def set_foods_lite(message: Message, state: FSMContext):
    await state.set_state(FSMFillForm.go_after_dop_f)
    #  написать похожее на то, что снизу. это выводится после go_dop и должно сделать расчет и внести в таблицу opera_vals
    food_weight = message.text
    food_name = opera_food_users.show_elem([f'{message.from_user.id}'], 'user_id', [f'opera_food_name'])[0][0]
    food_pars = foods.show_elem([f'{food_name}'], 'food_name', ['food_protein', 'food_fat', 'food_carbon', 'food_calorie'])[0]
    pars = consumed_now(food_pars[0], food_pars[1], food_pars[2], food_pars[3], food_weight)
    if message.from_user.id in opera_vals_users.show_id():
        late = opera_vals_users.show_str([f'{message.from_user.id}'])[0]
        opera_vals_users.change_full_str(f'{message.from_user.id}', [f'{pars[0] + late[1]}', f'{pars[1] + late[2]}', f'{pars[2] + late[3]}',f'{pars[3] + late[4]}'])
    elif message.from_user.id not in opera_vals_users.show_id():
        opera_vals_users.new_str(f'{message.from_user.id}', [f'{pars[0]}', f'{pars[1]}', f'{pars[2]}',f'{pars[3]}'])
    opera_food_users.del_str(f'{message.from_user.id}')
    await message.answer('Введи любую букву, чтобы продолжить')



@dp.message(StateFilter(FSMFillForm.go_append))
async def set_foods(message: Message, state: FSMContext):
    await state.set_state(FSMFillForm.go_after_append)
    pars_pre = str(message.text.lower()).split(' ')
    pars = consumed_now(pars_pre[0], pars_pre[1], pars_pre[2], pars_pre[3], pars_pre[4])
    food = opera_food_users.show_elem([f'{message.from_user.id}'], 'user_id', ['opera_food_name', 'opera_food_type'])[0]
    if message.from_user.id in opera_vals_users.show_id():
        late = opera_vals_users.show_str([f'{message.from_user.id}'])[0]
        opera_vals_users.change_full_str(f'{message.from_user.id}', [f'{pars[0] + late[1]}', f'{pars[1] + late[2]}', f'{pars[2] + late[3]}',f'{pars[3] + late[4]}'])
    elif message.from_user.id not in opera_vals_users.show_id():
        opera_vals_users.new_str(f'{message.from_user.id}', [f'{pars[0]}', f'{pars[1]}', f'{pars[2]}',f'{pars[3]}'])
    foods.new_str(f'{food[0]}', [f'{food[1]}', f'{pars_pre[3]}', f'{pars_pre[0]}', f'{pars_pre[1]}',f'{pars_pre[2]}'])
    opera_food_users.del_str(f'{message.from_user.id}')
    await message.answer('Введи любую букву, чтобы продолжить')



#  НАПИСАТЬ ДЛЯ ВЫВОДА ГРАФИКА -- call_feedback
@dp.callback_query(F.data == 'end', StateFilter(FSMFillForm.go_graph_r))
async def call_feedback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(default_state)
    w = (parameters.show_str([f'{callback.from_user.id}'])[0])[1:7]
    a, b, c, d, e, f = w[0], w[1], w[2], w[3], w[4], w[5]
    vals_r = calculate_macros(a, b, c, d, e, f)
    data = str(date.today()).split('-')
    vals_f = opera_vals_users.show_str([f'{callback.from_user.id}'])[0][1:5]
    graph_f = feedback_graph(callback.from_user.id, callback.from_user.first_name, data, vals_r, vals_f)
    vals_dif = difference(vals_r, vals_f)
    await callback.message.answer_photo(graph_f, caption=f'''Количество употребленных за день <i>калорий</i> <b><u>{vals_dif[0][0]}</u> {vals_dif[0][1]}</b> рекомендованного. \nОтношение употребленных <i>белков</i> <b><u>{vals_dif[1][0]}</u> {vals_dif[1][1]}</b> рекомендованного. \nОтношение употребленных <i>жиров</i> <b><u>{vals_dif[2][0]}</u> {vals_dif[2][1]}</b> рекомендованного. \nОтношение употребленных <i>углеводов</i> на <b><u>{vals_dif[3][0]}</u> {vals_dif[3][1]}</b> рекомендованного.\n\nНапиши любую букву для перехода на следующий шаг''', parse_mode='HTML')
    os.remove(f"graphs/graph_f{callback.from_user.id}.png")
    status.del_str_special(f"{'-'.join(data)}", f'{callback.from_user.id}')
    status.new_str(f'''{'-'.join(data)}''', [f'{callback.from_user.id}', f'{vals_f[0]}', f'{vals_f[1]}', f'{vals_f[2]}', f'{vals_f[3]}'])
    opera_vals_users.del_str(f'{callback.from_user.id}')
    await callback.answer()


# BLOCK input
@dp.callback_query(F.data == 'check', StateFilter(FSMFillForm.not_day))
async def input(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMFillForm.go_input)
    await bot.send_message(
        chat_id=f'{callback.from_user.id}',
        text='Введите дату через пробел (год месяц день):')



@dp.message(StateFilter(FSMFillForm.go_input))
async def call_stat(message: Message, state: FSMContext):
    await state.set_state(default_state)
    data = str(date.today()).split('-')
    vals_st = check_stat(f'''{'-'.join(data)}''', f'{message.from_user.id}')
    graph_st = status_graph(message.from_user.id, message.from_user.first_name, data, vals_st)
    await message.answer_photo(graph_st, caption='Напиши любую букву для перехода на следующий шаг')
    os.remove(f"graphs/graph_st{message.from_user.id}.png")



if __name__ == '__main__':
    dp.run_polling(bot)