from Domain.item import get_str, create_item
from Logic.add_string_to_description import append_str_to_price_above
from Logic.crud import create, update, delete
from Logic.most_expensive_from_location import get_highest_price_at_location
from Logic.move_items import locations_list, update_items_location
from Logic.order_ascending_price import order_ascending_by_price
from Logic.total_worth_in_location import sum_of_all_prices_in_a_place
from Logic.undo_redo import do_undo, do_redo
from UserInterface.console_ui import run_console_ui


def show_menu():
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


def handle_crud():
    print('')
    print('1. Add item')
    print('2. Change item')
    print('3. Delete item')
    print('a. Show all items')
    print('b. Return to main menu')
    print('')


def handle_show_all(items):
    for item in items:
        print(get_str(item))


def handle_add(item_list, undo, redo):
    obj_id = int(input("Enter item ID: "))
    obj_name = input("Enter item name: ")
    obj_desc = input("Enter item description: ")
    obj_pur_price = float(input("Enter item purchase price: "))
    obj_location = input("Enter item location: ")
    print('item succesfully added!')
    return create(item_list, obj_id, obj_name, obj_desc, obj_pur_price, obj_location, undo, redo)


def handle_change(item_list, undo, redo):
    to_be_changed_id = int(input("Enter the item's ID you'd like to change: "))
    to_be_changed_name = input("Enter the item's new name: ")
    to_be_changed_desc = input("Enter the item's new description: ")
    to_be_changed_pur_price = float(input("Enter the item's new purchase price: "))
    to_be_changed_loc = input("Enter the item's new item location: ")
    new_item = create_item(to_be_changed_id, to_be_changed_name, to_be_changed_desc,
                           to_be_changed_pur_price, to_be_changed_loc)
    print('Changes have been made!')
    return update(item_list, new_item, undo, redo)


def handle_delete(item_list, undo, redo):
    item_id = int(input("Enter item ID to be deleted: "))
    print('Deleted succesfully!')
    return delete(item_list, item_id, undo, redo)


def run_crud_ui(item_list, undo, redo):
    while True:
        handle_crud()
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


def handle_move(items, undo, redo):
    print(f"Used locations are: {locations_list(items)}.")
    move_from = input("Enter the location from which you wish to move all items: ")
    move_to = input("Enter the location where you want the items to be moved: ")
    print("items have been moved succesfully!")
    return update_items_location(items, move_from, move_to, undo, redo)


def handle_add_str_do_description(items):
    threshold_price = int(input("Enter the minimum price of items whose description will be modified: "))
    add_string = input("Now enter a string to add to the end of their descriptions: ")
    print("Descriptions have been updated!")
    return append_str_to_price_above(items, threshold_price, add_string)


def handle_max_price_in_location(items):
    print(f"Used locations are: {locations_list(items)}.")
    from_location = input("Enter the location where you want to see the most expensive item/items: ")
    print("Most expensive item/items from this location are: ")
    for item in get_highest_price_at_location(items, from_location):
        print(item)


def handle_order_ascending(items):
    print("The items have been ordered!")
    for item in order_ascending_by_price(items):
        print(item)


def handle_total_worth(items):
    print(f"Used locations are: {locations_list(items)}.")
    from_location = input("Enter the location from where you want to determine the total worth of the items: ")
    print(f"The total worth of all the items at this location is {sum_of_all_prices_in_a_place(items, from_location)}.")


def handle_undo(item_list, undo, redo):
    undo_result = do_undo(undo, redo, item_list)
    if undo_result is not None:
        return undo_result
    return item_list


def handle_redo(item_list, undo, redo):
    redo_result = do_redo(undo, redo, item_list)
    if redo_result is not None:
        return redo_result
    return item_list


def run_menu_ui():
    item_list = []
    undo = []
    redo = []
    while True:
        handle_show_all(item_list)
        show_menu()
        ui_command = input("Enter an option: ")
        if ui_command == '1':
            item_list = run_crud_ui(item_list, undo, redo)
        elif ui_command == '2':
            handle_move(item_list, undo, redo)
        elif ui_command == '3':
            handle_add_str_do_description(item_list)
        elif ui_command == '4':
            handle_max_price_in_location(item_list)
        elif ui_command == '5':
            handle_order_ascending(item_list)
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
