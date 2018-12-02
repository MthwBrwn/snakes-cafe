from textwrap import dedent
import sys


# collection of questions for the user
# looking to set up a list
# food_menu = [
#     {'food item': 'Wings', 'num_selected': 0},
#     {'food item': 'Cookies', 'num_selected': 0},
#     {'food item': 'Spring Rolls', 'num_selected': 0},
#     {'food item': 'Salmon', 'num_selected': 0},
#     {'food item': 'Steak', 'num_selected': 0},
#     {'food item': 'Meat Tornado', 'num_selected': 0},
#     {'food item': 'A Literal Garden', 'num_selected': 0},
#     {'food item': 'Ice cream', 'num_selected': 0},
#     {'food item': 'Cake', 'num_selected': 0},
#     {'food item': 'Pie', 'num_selected': 0},
#     {'food item': 'Coffee', 'num_selected': 0},
#     {'food item': 'Tea', 'num_selected': 0},
#     {'food item': 'Blood of the Innocent', 'num_selected': 0}
# ]


# food_menu = {'Wings': [0, Appetizers],
# 'Cookies': [0, Appetizers],
# 'Spring Rolls': 0,
# 'Salmon': 0,
# 'Steak': 0,
# 'Meat Tornado': 0,
# }

WIDTH = 60,


# upon review of the code there is no need for the simple lines to be
def line():
    """ This creates the line used in the welcome message """
    print (f'''
    {"*" * WIDTH}
    ''')
# def
#  (f'{"*" * (WIDTH)}')
# print (long_line)

# def empty():
#     """This is a line that a left side space to match the layout picture """
#     print (dedent(f'{"**"}'))


# def short_break():
#     """ another line used to match layout picture"""
#     print (dedent(f'{"-"* 8}'))


# def welcome(question):
#     """ print an intro message and the menu for the restaurant
#     """
#     print (dedent(f'{"**" + " " * ((WIDTH - 2 -len(question))//2) + question + " " * ((WIDTH - 4 - len(question))//2) + "**"}'))

def user_query():
    """ """
    print (' ')
    line()
    # welcome('What would you like to order?')
    line()
    input('??')


# def counter(x):
#     """ counter keeps the user's selection """
#     if str(x).lower() == 'quit':
#         exit()
#     for i in food_menu:
#         check = ''
#         check = (i['food item'])
#         if str(x).lower() == check.lower():
#             i['num_selected'] += i['num_selected']+1
#             print (i['num_selected'])
#     print('that doesn\'t seem to be an item.')


def exit():
    """Exit completes program with a message to user"""
    print ('Thank you for looking at our menu!')


# def print_items(food_type, i, j):
#     """ this sets up the menu items and gives some
#     flexibility to the menu items X is the food type and i and j
#     are the range for printing the food items"""
#     print(' ')
#     print(food_type)
#     short_break()
#     for k in range(i, j):
#         print (food_menu[k]['food item'])


def questionBlock():
    """ this establishes the text of the initial welcome page """
    line()
    # welcome('Welcome to the Snakes Cafe!')
    # welcome('Please see our menu below')
    # empty()
    # welcome('To quit at any time, type "quit"')
    line()


# def menu_format():
#     """ This is used to quickly print the items for user selection"""
#     if menu
#     print_items('Appetizers', 0, 3)
#     print_items('Entrees', 3, 7)
#     print_items('Desserts', 7, 10)
#     print_items('Drinks', 10, 13)


def run():
    """ run handles the call stack of the application """
    questionBlock()
    # menu_format()

    # order = None
    # while order is not 'quit'
    # user_input = user_query()
    # print(user_input)
    # counter(user_input)


if __name__ == '__main__':
    run()
