from textwrap import dedent
import sys

WIDTH = 60

# collection of questions for the user
# looking to set up a list
food_menu = [
    { 'food item' : 'Wings', 'num_selected': 0 },
    { 'food item' : 'Cookies', 'num_selected': 0 },
    { 'food item' : 'Spring Rolls', 'num_selected': 0 },
    { 'food item' : 'Salmon', 'num_selected': 0 },
    { 'food item' : 'Steak', 'num_selected': 0 },
    { 'food item' : 'Meat Tornado', 'num_selected': 0 },
    { 'food item' : 'A Literal Garden', 'num_selected': 0 },
    { 'food item' : 'Ice cream', 'num_selected': 0 },
    { 'food item' : 'Cake', 'num_selected': 0 },
    { 'food item' : 'Pie', 'num_selected': 0 },
    { 'food item' : 'Coffee', 'num_selected': 0 },
    { 'food item' : 'Tea', 'num_selected': 0 },
    { 'food item' : 'Blood of the Innocent', 'num_selected': 0 }
]

""" short functions for building questions()"""
def line():
    print (dedent(f'''{'*' * WIDTH} '''))

def empty ():
     print (dedent(f'''{'**'}  '''))

def short_break():
    print (dedent(f'''{'-'* 8}'''))

def welcome (question):
    """ print an intro message and the menu for the restaurant
    pass
    """
    print (dedent(f'''
        {'**' + ' ' * ((WIDTH - 2 -len(question))//2) + question + ' ' * ((WIDTH - 4 -len(question))//2) + '**'
        }
    '''))


def user_query ():
    print (' ')
    line()
    welcome('What would you like to order?')
    line()
    input('??')


def counter (x):

    if str(x).lower() == 'quit' :
            exit()
    for i in food_menu:
        check =''
        check = (i['food item'])
        if str(x).lower() == check.lower():
            i['num_selected'] += i['num_selected']+1
            print (i['num_selected'])
    print('that doesnt seem to be an item.')


def exit ():
    print ('Thank you for looking at our menu!')


""" this sets up the menu items and gives some flexibility to the menu items X is the food type and i and j are the range for printing the food items"""
def print_items (food_type,i,j):
    print(' ')
    print(food_type)
    short_break()
    for k in range (i,j):
        print (food_menu[k]['food item'])


def questionBlock ():
    line()
    welcome('Welcome to the Snakes Cafe!')
    welcome('Please see our menu below')
    empty()
    welcome('To quit at any time, type "quit"')
    line()


def menu_format():
    print_items('Appetizers',0,3)
    print_items('Entrees',3,7)
    print_items('Desserts',7,10)
    print_items('Drinks',10,13)


def run ():
        questionBlock ()
        menu_format ()
        user_input = user_query()
        print(user_input)
        counter(user_input)




if __name__ =='__main__':
    run()
