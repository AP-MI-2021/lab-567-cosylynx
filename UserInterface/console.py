from Domain.object import get_str, create_object
from Logic.crud import create, update, delete
from Logic.functionality import locations_list, update_objects_location, append_str_to_price_above


def show_menu():
    print('')
    print('1. CRUD (Create Read Update Delete)')
    print('2. Moving all objects from one location to another')
    print('3. Adding a string to the description of objects with the price greater than a value')
    # print('5. ')
    # print('6. ')
    # print('7. ')
    print('a. Show all objects')
    print('x. Exit Program')
    print('')


def handle_crud():
    print('')
    print('1. Add object')
    print('2. Change object')
    print('3. Delete object')
    print('a. Show all objects')
    print('b. Return to main menu')
    print('')


def handle_show_all(objects):
    for object in objects:
        print(get_str(object))


def handle_add(object_list):
    obj_id = int(input("Enter object ID: "))
    obj_name = input("Enter object name: ")
    obj_desc = input("Enter object description: ")
    obj_pur_price = int(input("Enter object purchase price: "))
    obj_location = input("Enter object location: ")
    print('Object succesfully added!')
    return create(object_list, obj_id, obj_name, obj_desc, obj_pur_price, obj_location)


def handle_change(object_list):
    to_be_changed_id = int(input("Enter the object's ID you'd like to change: "))
    to_be_changed_name = input("Enter the object's new name: ")
    to_be_changed_desc = input("Enter the object's new description: ")
    to_be_changed_pur_price = int(input("Enter the object's new purchase price: "))
    to_be_changed_loc = input("Enter the object's new object location: ")
    new_object = create_object(to_be_changed_id, to_be_changed_name, to_be_changed_desc,
                               to_be_changed_pur_price, to_be_changed_loc)
    print('Changes have been made!')
    return update(object_list, new_object)


def handle_delete(object_list):
    object_id = int(input("Enter object ID to be deleted: "))
    print('Deleted succesfully!')
    return delete(object_list, object_id)


def run_crud_ui(object_list):
    while True:
        handle_crud()
        ui_command = input("Enter an option: ")
        if ui_command == '1':
            object_list = handle_add(object_list)
        elif ui_command == '2':
            object_list = handle_change(object_list)
        elif ui_command == '3':
            object_list = handle_delete(object_list)
        elif ui_command == 'a':
            handle_show_all(object_list)
        elif ui_command == 'b':
            return object_list
        else:
            print("Invalid command! Please try again!")


def handle_move(objects):
    print(f"Used locations are: {locations_list(objects)}.")
    move_from = input("Enter the location from which you wish to move all objects: ")
    move_to = input("Enter the location where you want the objects to be moved: ")
    return update_objects_location(objects, move_from, move_to)


def handle_add_str_do_description(objects):
    threshold_price = int(input("Enter the minimum price of objects whose description will be modified: "))
    add_string = input("Now enter a string to add to the end of their descriptions: ")
    return append_str_to_price_above(objects, threshold_price, add_string)


def run_main_ui():
    object_list = []
    while True:
        show_menu()
        ui_command = input("Enter an option: ")
        if ui_command == '1':
            object_list = run_crud_ui(object_list)
        elif ui_command == '2':
            handle_move(object_list)
        elif ui_command == '3':
            handle_add_str_do_description(object_list)
        elif ui_command == 'a':
            handle_show_all(object_list)
        elif ui_command == 'x':
            break
        else:
            print("Invalid command! Please try again!")
