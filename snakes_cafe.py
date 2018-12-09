from textwrap import dedent
import sys


# dictionary-
# --------------
food_menu = {
    'APPETIZERS': {
        'Cookies': 0,
        'Salmon': 0,
        'Spring Rolls': 0,
    },
    'ENTREES': {
        'Steak': 0,
        'Meat Tornado': 0,
        'A Literal Garden': 0,
    },
    'DESSERTS': {
        'Ice cream': 0,
        'Cake': 0,
        'Pie': 0,
    },
    'DRINKS': {
        'Coffee': 0,
        'Tea': 0,
        'Wings': 0,
        'Blood of the Innocent': 0,
    }
}

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


def questionBlock():
    """ this establishes the text of the initial welcome page """
    long_line()
    welcome('Welcome to the Snakes Cafe!')
    welcome('Please see our menu below')
    empty()
    welcome(' To quit at any time, type "quit"')
    long_line()


# def counter(x):
#     """ counter keeps the user's selection """
#     if str(x).lower() == 'quit':
#         exit()
#     for i in food_menu:
#         check = ''
#         check = (i['food item'])
#         if str(x).lower() == check.lower():
#             i['num_selected'] += i['num_selected']+1
#             print(i['num_selected'])
#     print('that doesn\'t seem to be an item.')


def exit():
    """Exit completes program with a message to user"""
    print('Thank you for looking at our menu!')


def print_items():
    """ this sets up the menu items and gives some
    flexibility to the menu items - New menu items could be added to list.
    """
    print(' ')
    short_break()
    for type in food_menu:
        print(type)
        short_break()
        for item in food_menu[type]:
            print(item)
        short_break()


def user_query():
    """ """
    print(' ')
    long_line()
    welcome('What would you like to order?')
    long_line()
    input('??')
    return input




# def menu_format():
#     """ This is used to quickly print the items for user selection"""

#     print_items('Appetizers', 0, 3)
#     print_items('Entrees', 3, 7)
#     print_items('Desserts', 7, 10)
#     print_items('Drinks', 10, 13)


def run():
    """ run handles the call stack of the application """
    questionBlock()
    print_items()
    # menu_format()
    user_input = None
    while user_input is not 'quit':
        user_query()
        # counter(user_input)


if __name__ == '__main__':
    run()
