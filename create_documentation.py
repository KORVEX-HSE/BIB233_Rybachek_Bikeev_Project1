from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


def calculator_1(age:int,hight:int,wight:int,life_style,gender:str):
    """Calculates the total calorie requirement to maintain weight
    :param age: age of a person
    :type age: int
    :param hight: height of a person
    :type hight: int
    :param wight: weight of a person
    :type wight: int
    :param life_style: the level of physical activity
    :type life_style: str
    :param gender: gender of a person
    :type gender: str
    :return: the total calorie requirement to maintain weight
    :rtype: int
    """

def calculate_macros( age:int,hight:int,wight:int,life_style,gender:str,goal:str):
    """Calculates the macronutrient distribution for a specific goal
    :param age: age of a person
    :type age: int
    :param hight: height of a person
    :type hight: int
    :param wight: weight of a person
    :type wight: int
    :param life_style: the level of physical activity
    :type life_style: str
    :param gender: gender of a person
    :type gender: str
    :param goal: goal of nutrition (gain, loss, balance)
    :type goal: str
    :return: the distribution of macronutrients
    :rtype: str
    """


def consumed_now(pr_wight,pr_cal,pr_prot,pr_fat,pr_carb):
    """Calculates the total amount of calories, protein, fat, and carbohydrates consumed based on the weight and nutritional values of a food product
    :param pr_wight: the weight of the food product in grams
    :type pr_wight: int
    :param pr_cal: the calorie content of the food product per 100 grams
    :type pr_cal: int
    :param pr_prot: the protein content of the food product per 100 grams
    :type pr_prot: int
    :param pr_fat: the fat content of the food product per 100 grams
    :type pr_fat: int
    :param pr_carb: the carbohydrate content of the food product per 100 grams
    :type pr_carb: int
    :return: a tuple containing the total calories, protein, fat, and carbohydrates consumed
    :rtype: tuple
    """


def difference(vals_r, vals_f):
    """
    Returns the difference between the values vals_f and vals_r which shows how much he has gained in calories

    :param vals_r:  The list of calculated values
    :type vals_r: list of int
    :param vals_f: The list of actual values
    :type vals_f: list of int
    :return: The list is the difference between vals_f and vals_r
    :rtype: list of list
    """

async def new_str(self, id: str, value: list[str]) -> None:

    '''Adding a row to a table
    \nlist[str] - values of all columns except id
    \nIt looks like ['col_1', 'col_2', 'col_3', .......]

    :param id: the unique identifier of the string
    :type id: str
    :param value: column values other than id
    :type value: list[str]
    :return: None
    :rtype: None
    '''


async def del_str(self, id: str) -> None:

    '''Deletes a row from the table by its id.

    :param id: Line ID
    :type id: str
    :return: None
    '''    

async def del_str_special(self, datas: str, user_id: str) -> None:

    '''Special deletion of a row with a specific date and id for the status table.

    :param datas: Date of the line
    :type datas: str
    :param user_id: User ID
    :type user_id: str
    :return: None
    '''

async def change_one_str(self, id: str, col: str, value: str) -> None:

    '''Replaces one element from one column in a row by its id.

    :param id: Line ID
    :type id: str
    :param col: Column name
    :type col: str
    :param value: The new value of the element
    :type value: str
    :return: None
    '''


async def change_full_str(self, id: str, value: list) -> None:
    """Replacing all elements in a row by its id (except the id itself)

    :param self: class object
    :type self: object
    :param id: line id
    :type id: str
    :param value: values of all columns except id
    :type value: list[str]
    :return: None
    :rtype: None
    """



async def show_col(self, cols: list[str]) -> list:
    """Returns all elements of columns(columns) by their names

    :param self: class object
    :type self: object
    :param cols: a list of the names of the necessary columns
    :type cols: list[str]
    :return: list of column elements
    :rtype: list
    """


async def show_str(self, lines: list[str]) -> list:
    """Returns all row elements by their id
    As input accepts a list of the id of the required rows
    
    :param lines: list of id of required lines
    :type lines: list[str]
    :return: list of row elements
    :rtype: list
    """
    
async def show_elem(self, lines: list[str], lines_from_col: str, cols: list[str]) -> list:
    """Returns all elements from the intersection of rows (by id) and columns (by name)
    First accepts as input a list of the ids of the desired rows
    Then it takes as input the name of the column in which these ids are
    Then it accepts a list of the names of the necessary columns as input
    
    :param lines: list of id of required lines
    :type lines: list[str]
    :param lines_from_col: column name with id
    :type lines_from_col: str
    :param cols: list of column names
    :type cols: list[str]
    :return: a list of elements from the intersection of rows and columns
    :rtype: list
    """


async def show_table(self) -> list:
    """Returns the data from the table as a list of tuples

    :return: data from the table
    :rtype: list
    """
    

async def show_id(self) -> list:
    """Returns a list of IDs from the table

    :return: list of IDs
    :rtype: list
    """


async def process_start_command_mess(message: Message, state: FSMContext):
    """Processes the start command message

    :param message: the incoming message
    :type message: Message
    :param state: current state
    :type state: FSMContext
    """



async def process_start_command_call(message: Message, state: FSMContext):
    """Processes the start command call message

    :param message: the incoming message
    :type message: Message
    :param state: current state
    :type state: FSMContext
    """


async def norm_pfc(callback: CallbackQuery, state: FSMContext):
    """Sets the state to FSMFillForm.day if the data received is 'newday' and the current state is not FSMFillForm.day.

    :param callback: The callback query received
    :param state: The state context associated with the query
    :return: None
    :rtype: None
    :raises: No specific exception is raised
    """

async def gender_user(callback: CallbackQuery, state: FSMContext):
    """Changes the state to FSMFillForm.gorec if the data received is 'PFC' and the current state is FSMFillForm.day.

    :param callback: The callback query received
    :param state: The state context associated with the query
    :return: None
    :rtype: None
    :raises: No specific exception is raised
    """

async def ahw_user(callback: CallbackQuery, state: FSMContext):
    """Changes the state to FSMFillForm.go_gen if the data received is 'man' or 'woman' and the current state is FSMFillForm.go_rec.

    :param callback: The callback query received
    :param state: The state context associated with the query
    :return: None
    :rtype: None
    :raises: No specific exception is raised
    """

async def style_life(message: Message, state: FSMContext):
    """Changes the state to FSMFillForm.go_ahw upon receiving a message if the current state is FSMFillForm.go_gen. It also updates the age, height, and weight parameters based on the user input.

    :param message: The message received
    :param state: The state context associated with the message
    :return: None
    :rtype: None
    :raises: No specific exception is raised
    """

async def goal(callback: CallbackQuery, state: FSMContext):
    """Changes the state to FSMFillForm.go_style and updates the 'life_style' parameter based on the data received. It also edits the message to prompt the user to select their goal.

    :param callback: The callback query received
    :param state: The state context associated with the query
    :return: None
    :rtype: None
    :raises: No specific exception is raised
    """

async def call_recomendation(callback: CallbackQuery, state: FSMContext):
    """Changes the state to FSMFillForm.go_goal and updates the 'mission' parameter based on the data received. It then calculates and displays the recommended daily caloric intake based on the user's input.

    :param callback: The callback query received
    :param state: The state context associated with the query
    :return: None
    :rtype: None
    :raises: No specific exception is raised
    """

async def call(message: Message, state: FSMContext):
    """
    This function handles the call message and sets the state to go_graph_r in the FSMFillForm state machine. It also sends a message to the user to choose an action.

    :param message: The incoming message from the user
    :type message: Message
    :param state: The FSM state context
    :type state: FSMContext
    """
    


async def fixat(callback: CallbackQuery, state: FSMContext):
    """
    This function handles the fix callback query and sets the state to go_fix in the FSMFillForm state machine. It also sends a message to the user to choose a group of products.

    :param callback: The callback query from the user
    :type callback: CallbackQuery
    :param state: The FSM state context
    :type state: FSMContext
    """

async def type_name(callback: CallbackQuery, state: FSMContext):
    """
    This function handles the callback queries for different food groups. It sets the state to go_groups in the FSMFillForm state machine and updates the user's food type choice.

    :param callback: The callback query from the user
    :type callback: CallbackQuery
    :param state: The FSM state context
    :type state: FSMContext
    """
    

async def app_food(message: Message, state: FSMContext):
    """
    This function handles the message for entering a food name. It updates the user's food name choice and sets the state to go_dop if the food product exists in the database, or to go_new if it doesn't.

    :param message: The incoming message from the user
    :type message: Message
    :param state: The FSM state context
    :type state: FSMContext
    """

async def type_not_full(message: Message, state: FSMContext):
    """
    Sends a message to the user requesting the amount of a previously indicated food product in grams.

    :param message: the message object sent by the user
    :type message: Message
    :param state: the current state of the FSM
    :type state: FSMContext
    :return: None
    :rtype: None
    """
    

async def type_full(callback: CallbackQuery, state: FSMContext):
    """
    Sends a message to the user requesting the values of protein, fat, carbohydrates in grams, the amount of calories per 100 grams, and the weight in grams of the consumed food product.

    :param callback: the callback query object sent by the user
    :type callback: CallbackQuery
    :param state: the current state of the FSM
    :type state: FSMContext
    :return: None
    :rtype: None
    """

async def set_foods_lite(message: Message, state: FSMContext):
    """Updates user's consumed values based on the entered food weight

    :param message: the message containing the food weight
    :type message: Message
    :param state: the current state of the conversation
    :type state: FSMContext
    :return: None
    :rtype: None
    """
    

async def set_foods(message: Message, state: FSMContext):
    """Updates user's consumed values and adds new food to the database

    :param message: the message containing the food parameters
    :type message: Message
    :param state: the current state of the conversation
    :type state: FSMContext
    :return: None
    :rtype: None
    """


async def set_foods_lite(message: Message, state: FSMContext):
    """Updates user's consumed values based on the entered food weight

    :param message: the message containing the food weight
    :type message: Message
    :param state: the current state of the conversation
    :type state: FSMContext
    :return: None
    :rtype: None
    """
    

async def set_foods(message: Message, state: FSMContext):
    """Updates user's consumed values and adds new food to the database

    :param message: the message containing the food parameters
    :type message: Message
    :param state: the current state of the conversation
    :type state: FSMContext
    :return: None
    :rtype: None
    """

async def call_feedback(callback: CallbackQuery, state: FSMContext):
    """Generates feedback graph and sends the user consumed values and recommended values

    :param callback: the callback query containing the user data
    :type callback: CallbackQuery
    :param state: the current state of the conversation
    :type state: FSMContext
    :return: None
    :rtype: None
    """
    

async def input(callback: CallbackQuery):
    """Sends a message to the user with a specific keyboard for input

    :param callback: the callback query containing the user data
    :type callback: CallbackQuery
    :return: None
    :rtype: None
    """
    