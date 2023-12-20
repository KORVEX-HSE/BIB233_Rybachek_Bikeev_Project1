import matplotlib.pyplot as plt
from aiogram.types import FSInputFile
from SQL_class import *
import os



status = Table('status', ['datas', 'user_id', 'st_prot', 'st_fat', 'st_carb', 'st_cal'])



def recomend_graph(id, first_name, data, vals_r):

    monthes = {1:'января',2:'февраля',3:'марта',4:'апреля',5:'мая',6:'июня',7:'июля',8:'августа',9:'сентября',10:'октября',11:'ноября',12:'декабря'}
    month_name = monthes[int(data[1])]

    plt.figure()

    labels = ['Белки', 'Жиры', 'Углеводы']

    fig, ax = plt.subplots()
    ax.pie(vals_r[0:3], labels=labels, wedgeprops=dict(width=0.7), autopct='%1.0f%%')
    plt.title(f'Диаграмма рекомендованного БЖД для {first_name} \nза {data[2]} {month_name} {data[0]}')

    #  Сохраняем график в файл
    plt.savefig(f'graphs/graph_r{id}.png')

    #  Присваиваем переменной график
    graph_r = FSInputFile(f"graphs/graph_r{id}.png")

    return graph_r



def feedback_graph(id, first_name, data, vals_r, vals_f):
    monthes = {1:'января',2:'февраля',3:'марта',4:'апреля',5:'мая',6:'июня',7:'июля',8:'августа',9:'сентября',10:'октября',11:'ноября',12:'декабря'}
    month_name = monthes[int(data[1])]
    
    plt.figure()

    labels = ['Белки', 'Жиры', 'Углеводы']

    fig, axs = plt.subplots(nrows= 1 , ncols= 2 )
    
    axs[0].pie(vals_r[0:3], labels=labels, wedgeprops=dict(width=0.7), autopct='%1.0f%%')
    axs[1].pie(vals_f[0:3], labels=labels, wedgeprops=dict(width=0.7), autopct='%1.0f%%')

    fig.suptitle(f'Диаграммы БЖД \nдля {first_name} \nза {data[2]} {month_name} {data[0]}')

    axs[0].set_title('Рекомендованное')
    axs[1].set_title('Фактическое')


    # Сохраняем график в файл
    plt.savefig(f'graphs/graph_f{id}.png')

    #  Присваиваем переменной график
    graph_f = FSInputFile(f"graphs/graph_f{id}.png")

    return graph_f
    



def status_graph(id, first_name, data, vals_st):

    monthes = {1:'января',2:'февраля',3:'марта',4:'апреля',5:'мая',6:'июня',7:'июля',8:'августа',9:'сентября',10:'октября',11:'ноября',12:'декабря'}
    month_name = monthes[int(data[1])]

    plt.figure()

    labels = ['Белки', 'Жиры', 'Углеводы']

    fig, ax = plt.subplots()
    ax.pie(vals_st[0:3], labels=labels, wedgeprops=dict(width=0.7), autopct='%1.0f%%')
    plt.title(f'Диаграмма фактического БЖД для {first_name} \nза {data[2]} {month_name} {data[0]}')

    #  Сохраняем график в файл
    plt.savefig(f'graphs/graph_st{id}.png')

    #  Присваиваем переменной график
    graph_st = FSInputFile(f"graphs/graph_st{id}.png")

    return graph_st