from textwrap import dedent
import sys


# dictionary-
# --------------
food_menu = {
    'Appetizers': {
        'Cookies': 0,
        'Salmon': 0,
        'Spring Rolls': 0,
    },
    'Entrees': {
        'Steak': 0,
        'Meat Tornado': 0,
        'A Literal Garden': 0,
    },
    'Desserts': {
        'Ice cream': 0,
        'Cake': 0,
        'Pie': 0,
    },
    'Drinks': {
        'Coffee': 0,
        'Tea': 0,
        'Wings': 0,
        'Blood of the Innocent': 0,
    }
}


# food_menu = {'Wings': [0, Appetizers],
# 'Cookies': [0, Appetizers],
# 'Spring Rolls': 0,
# 'Salmon': 0,
# 'Steak': 0,
# 'Meat Tornado': 0,
# }

WIDTH = 60


def long_line():
    """ This creates the line used in the welcome message """
    print(f"{'*' * WIDTH}")


def empty():
    """This is a line that a left side space to match the layout picture """
    print(dedent(f'{"**" + " " * (WIDTH-4) + "**"}'))


def short_break():
    """ another line used to match layout picture"""
    print(dedent(f'{"-"* 8}'))


def welcome(question):
    """ print an intro message and the menu for the restaurant
    """
    print(dedent(f'{"**" + " " * ((WIDTH - 2 -len(question))//2) + question + " " * ((WIDTH - 4 - len(question))//2) + "**"}'))


def user_query():
    """ """
    print(' ')
    long_line()
    welcome('What would you like to order?')
    long_line()
    input('??')
    return input


def counter(x):
    """ counter keeps the user's selection """
    if str(x).lower() == 'quit':
        exit()
    for i in food_menu:
        check = ''
        check = (i['food item'])
        if str(x).lower() == check.lower():
            i['num_selected'] += i['num_selected']+1
            print(i['num_selected'])
    print('that doesn\'t seem to be an item.')


def exit():
    """Exit completes program with a message to user"""
    print('Thank you for looking at our menu!')


def print_items(key):
    """ this sets up the menu items and gives some
    flexibility to the menu items X is the food type and i and j
    are the range for printing the food items"""
    print(' ')
    short_break()
    for k in range(lenfood_menu):
        print(food_menu ])


def questionBlock():
    """ this establishes the text of the initial welcome page """
    long_line()
    welcome('Welcome to the Snakes Cafe!')
    welcome('Please see our menu below')
    empty()
    welcome(' To quit at any time, type "quit"')
    long_line()


def menu_format():
    """ This is used to quickly print the items for user selection"""

    print_items('Appetizers', 0, 3)
    print_items('Entrees', 3, 7)
    print_items('Desserts', 7, 10)
    print_items('Drinks', 10, 13)


def run():
    """ run handles the call stack of the application """
    questionBlock()
    menu_format()
    user_input = None
    while user_input is not 'quit':
        user_input = user_query
        counter(user_input)


if __name__ == '__main__':
    run()
