from UserInterface.console_ui import run_console_ui
from UserInterface.ui import *


def show_main_menu():
    print('')
    print('1. CRUD (Create Read Update Delete)')
    print('2. Moving all items from one location to another')
    print('3. Adding a string to the description of items with the price greater than a value')
    print('4. Determine the most expensive item from a location')
    print('5. Order objects in ascending order by purchase price')
    print('6. Determine the total worth of items from one location')
    print('u. Undo')
    print('r. Redo')
    print('a. Show all items')
    print('x. Exit Program')
    print('')


def run_menu_ui():
    item_list = []
    undo = []
    redo = []
    while True:
        try:
            handle_show_all(item_list)  # to delete this line after undo redo working correctly
            show_main_menu()
            ui_command = input("Enter an option: ")
            if ui_command == '1':
                item_list = run_crud_ui(item_list, undo, redo)
            elif ui_command == '2':
                handle_move(item_list, undo, redo)
            elif ui_command == '3':
                handle_add_str_do_description(item_list, undo, redo)
            elif ui_command == '4':
                handle_max_price_in_location(item_list)
            elif ui_command == '5':
                handle_order_ascending(item_list, undo, redo)
            elif ui_command == '6':
                handle_total_worth(item_list)
            elif ui_command == 'u':
                item_list = handle_undo(item_list, undo, redo)
            elif ui_command == 'r':
                item_list = handle_redo(item_list, undo, redo)
            elif ui_command == 'a':
                handle_show_all(item_list)
            elif ui_command == 'x':
                break
            else:
                print("Invalid command! Please try again!")
        except Exception as ex:
            print(f"Error: {ex}")


def show_crud_menu():
    print('')
    print('1. Add item')
    print('2. Change item')
    print('3. Delete item')
    print('a. Show all items')
    print('b. Return to main menu')
    print('')


def run_crud_ui(item_list, undo, redo):
    while True:
        try:
            show_crud_menu()
            ui_command = input("Enter an option: ")
            if ui_command == '1':
                item_list = handle_add(item_list, undo, redo)
            elif ui_command == '2':
                item_list = handle_change(item_list, undo, redo)
            elif ui_command == '3':
                item_list = handle_delete(item_list, undo, redo)
            elif ui_command == 'a':
                handle_show_all(item_list)
            elif ui_command == 'b':
                return item_list
            else:
                print("Invalid command! Please try again!")
        except Exception as ex:
            print(f"Error: {ex}")

def run_ui():
    print("")
    option = input("1. Interactive\n"
                   "2. Console mode\n"
                   "Select an interface type: ")
    print("")
    if option == '1':
        run_menu_ui()
    elif option == '2':
        run_console_ui()
    else:
        print("No option has been selected. Bad input!")
