import psycopg2



try:
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='20dima006', host='localhost')
except:
    print('Can`t establish connection to database')


class Table():

    '''Содержит методы для управления таблицами в базе данных:
    \nnew_str           - Добавление строки в таблицу
    \ndel_str           - Удаление строки из таблицы по ее id
    \nchange_one_str    - Замена одного элемента из одной колонки в строке по ее id
    \nchange_full_str   - Замена всех элементов в строке по ее id (кроме самого id)
    \nshow_col          - Возвращает все элементы колонок по их названиям
    \nshow_str          - Возвращает все элементы строк по их id
    \nshow_elem         - Возвращает все элементы из пересечения строк (по id) и колонок (по названиям)
    \nshow_table        - Возвращает таблицу
    \nshow_id           - Возвращает список id'''


    def __init__(self, table: str, column: list) -> None:
        self.table = table
        self.column = column
    

    def new_str(self, id: str, value: list[str]) -> None:

        '''Добавление строки в таблицу
        \nlist[str] - значения всех колонок, кроме id
        \nВыглядит как ['col_1', 'col_2', 'col_3', .......]'''

        with conn.cursor() as cursor:
            for i in range(len(value)+1):
                if i == 0:
                    cursor.execute(f"""INSERT INTO {self.table} ({self.column[i]}) 
                                   VALUES ('{id}');""")
                else:
                    cursor.execute(f"""UPDATE {self.table} SET {self.column[i]}='{value[i-1]}' 
                                   WHERE {self.column[0]}='{id}';""")
            conn.commit()
    

    def del_str(self, id: str) -> None:

        '''Удаление строки из таблицы по ее id'''

        with conn.cursor() as cursor:
            cursor.execute(f"""DELETE FROM {self.table} 
                           WHERE {self.column[0]}='{id}';""")
            conn.commit()


    def del_str_special(self, datas: str, user_id: str) -> None:

        '''Специальное удаление строки с определенной датой и id для таблицы status'''

        with conn.cursor() as cursor:
            cursor.execute(f"""DELETE FROM {self.table} WHERE datas = '{datas}' and user_id = '{user_id}'""")

    
    def change_one_str(self, id: str, col: str, value: str) -> None:
        
        '''Замена одного элемента из одной колонки в строке по ее id
        \nПринимает сначала id строки
        \nПотом принимает название колонки
        \nПотом принимает новое значение элемента'''

        with conn.cursor() as cursor:
            cursor.execute(f"""UPDATE {self.table} SET {col}='{value}' 
                           WHERE {self.column[0]}='{id}';""")
            conn.commit()

    
    def change_full_str(self, id: str, value: list) -> None:
        
        '''Замена всех элементов в строке по ее id (кроме самого id)
        \nlist[str] - значения всех колонок, кроме id
        \nВыглядит как ['col_1', 'col_2', 'col_3', .......]'''

        with conn.cursor() as cursor:
            for i in range(1, len(value)+1):
                cursor.execute(f"""UPDATE {self.table} SET {self.column[i]}='{value[i-1]}' 
                               WHERE {self.column[0]}='{id}';""")
            conn.commit()
    

    def show_col(self, cols: list[str]) -> list:

        '''Возвращает все элементы колонок(столбцов) по их названиям
        \nНа вход принимает список из названий нужных колонок'''

        with conn.cursor() as cursor:
            res = list()
            for col in cols:
                cursor.execute(f"""SELECT {col} FROM {self.table};""")
                dop_res = cursor.fetchall()
                pre_res = list()
                for i in dop_res:
                    pre_res.append(i[0])
                res.append(pre_res)
            return res


    def show_str(self, lines: list[str]) -> list:

        '''Возвращает все элементы строк по их id
        \nНа вход принимает список из id нужных строк'''

        with conn.cursor() as cursor:
            res = list()
            for id in lines:
                cursor.execute(f"""SELECT * FROM {self.table} 
                               WHERE {self.column[0]}='{id}';""")
                res.append(list(cursor.fetchall()[0]))
            return res
    

    def show_elem(self, lines: list[str], lines_from_col: str, cols: list[str]) -> list:

        '''Возвращает все элементы из пересечения строк (по id) и колонок (по названиям)
        \nСначала принимает на вход список из id нужных строк
        \nПотом принимает на вход название колонки, в которой эти id
        \nЗатем принимет на вход список из названий нужных колонок'''

        with conn.cursor() as cursor:
            res = list()
            ind = self.column.index(lines_from_col)
            for key in lines:
                sub_res = list()
                for col in cols:
                    cursor.execute(f"""SELECT {col} FROM {self.table} 
                                   WHERE {self.column[ind]}='{key}';""")
                    dop_res = cursor.fetchall()
                    pre_res = list()
                    for i in dop_res:
                        pre_res.append(i[0])
                    sub_res.extend(pre_res)
                res.append(sub_res)
            return res
    

    def show_table(self) -> list:

        '''Возвращает таблицу'''

        with conn.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM {self.table};""")
            return cursor.fetchall()
    

    def show_id(self) -> list:

        '''Возвращает список id'''

        with conn.cursor() as cursor:
            cursor.execute(f"""SELECT {self.column[0]} FROM {self.table};""")
            pre_res = cursor.fetchall()
            res = list()
            for i in pre_res:
                res.append(i[0])
            return res
    

    def show_special_status(self, datas, user_id, type):

        '''Специальная функция возврата статистики за определенный день для status'''

        with conn.cursor() as cursor:
            cursor.execute(f"""SELECT {type} FROM {self.table} WHERE datas = '{datas}' and user_id = {user_id}""")
            return cursor.fetchall()[0][0]