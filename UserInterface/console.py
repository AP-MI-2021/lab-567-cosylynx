from Domain.object import get_str, create_object
from Logic.crud import create, update, delete


def show_menu():
    print('1. CRUD')
    print('2. Moving all objects from one location to another')
    # print('3. ')
    # print('4. ')
    # print('5. ')
    # print('6. ')
    # print('7. ')
    print('x. Exit Program')
    print('')


def handle_crud():
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
    to_be_changed_pur_price = input("Enter the object's new purchase price: ")
    to_be_changed_loc = input("Enter the object's new object location: ")
    new_object = create_object(to_be_changed_id, to_be_changed_name, to_be_changed_desc,
                               to_be_changed_pur_price, to_be_changed_loc)
    print('Changes have been made!')
    return update(object_list, new_object)


def handle_delete(object_list):
    object_id = int(input("Enter object ID to be deleted: "))
    print('Deleted succesfully!')
    return delete(object_list, object_id)


def run_crud_ui():
    object_list = []
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
            break
        else:
            print("Invalid command! Please try again!")


def run_main_ui():
    while True:
        show_menu()
        ui_command = input("Enter an option: ")
        if ui_command == '1':
            run_crud_ui()
        elif ui_command == '2':
            print('hi')
        elif ui_command == 'x':
            break
        else:
            print("Invalid command! Please try again!")

