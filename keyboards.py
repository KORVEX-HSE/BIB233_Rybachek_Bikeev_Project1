from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



# Клавиатура входа
start_countind_day = InlineKeyboardButton(
    text='Начать учет дня',
    callback_data='new_day')
view_statistics = InlineKeyboardButton(
    text='Посмотреть статистику',
    callback_data='check')  

keyboard_start = InlineKeyboardMarkup(
    inline_keyboard=[[start_countind_day],
                     [view_statistics]])



# Клавитаура входа в расчет БЖУ
calc_PFC = InlineKeyboardButton(
    text='Расчет БЖУ',
    callback_data = 'PFC')

keyboard_PFC = InlineKeyboardMarkup(
    inline_keyboard=[[calc_PFC]])



# Клавиатура пола
man = InlineKeyboardButton(
    text='Мужчина',
    callback_data='man')
woman = InlineKeyboardButton(
    text='Женщина',
    callback_data='woman')

keyboard_qender = InlineKeyboardMarkup(
    inline_keyboard=[[man],
                     [woman]])



# Клавиатура стиля жизни
very_low = InlineKeyboardButton(
    text='Сидячий или малополвижный',
    callback_data='very_low')
low = InlineKeyboardButton(
    text='Легкая активность 1-3 раза в неделю',
    callback_data='low')
middle = InlineKeyboardButton(
    text='Средняя активность 3-5 раз в неделю',
    callback_data='middle')
hard = InlineKeyboardButton(
    text='Тренеровки каждый день ',
    callback_data='hard')

keyboard_style = InlineKeyboardMarkup(
    inline_keyboard=[[very_low],
                     [low],
                     [middle],
                     [hard]])



# Клавивтура целей
gain_weight= InlineKeyboardButton(
    text='Набор массы',
    callback_data='gain')
balance_weight = InlineKeyboardButton(
    text='Поддержание веса',
    callback_data='balance')
loss_weight = InlineKeyboardButton(
    text='Уменьшение веса',
    callback_data='loss')

keyboard_goal = InlineKeyboardMarkup(
    inline_keyboard=[[gain_weight],
                     [balance_weight],
                     [loss_weight]])



# Клавиатура фиксации (после graph_r)
fixation = InlineKeyboardButton(
    text='Записать съеденное',
    callback_data = 'fix')
 
end_day = InlineKeyboardButton(
    text='Закончить день',
    callback_data = 'end')
 
keyboard_fixation = InlineKeyboardMarkup(
    inline_keyboard=[[fixation],
                     [end_day]])



# Клавиатура групп продуктов
t_1 = InlineKeyboardButton(
    text='Сладкое,в том числе сладкие напитки',
    callback_data = 'sweet')

t_2 = InlineKeyboardButton(
    text='Жиры разных типов',
    callback_data = 'fat_group')

t_3 = InlineKeyboardButton(
    text='Животные подукты',
    callback_data = 'animal')

t_4 = InlineKeyboardButton(
    text='Круппы',
    callback_data = 'group')

t_5 = InlineKeyboardButton(
    text='Свежие овощи и фрукты',
    callback_data = 'green')

t_6 = InlineKeyboardButton(
    text='Напитки без сахара',
    callback_data = 'no_sug_drink')

keyboard_groups = InlineKeyboardMarkup(
    inline_keyboard=[[t_1],
                     [t_2],
                     [t_3],
                     [t_4],
                     [t_5],
                     [t_6]])



# Клавиатура добавления продукта
Button_append = InlineKeyboardButton(
    text='Ввести данные',
    callback_data = 'append')
 
keyboard_append = InlineKeyboardMarkup(
    inline_keyboard=[[Button_append]])



# Клавиатура статистики
input_data = InlineKeyboardButton(
    text='Введите дату через пробел (год месяц день):',
    callback_data='data_way')

keyboard_input = InlineKeyboardMarkup(
    inline_keyboard=[[input_data]])