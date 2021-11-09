from Domain.item import get_str
from Logic.crud import *


def help_dialog():
    print("Usage: \n"
          "add,<id>,<name>,<description>,<purchase_price>,<location>;\n"
          "remove,<id>;\n"
          "update,<id>,<name>,<description>,<purchase_price>,<location>;\n"
          "showall;\n"
          "exit;\n"
          "Use ',' to separate the arguments of a command and ';' to mark the end of the command.\n"
          "\n"
          "Available commands are:\n"
          "add, remove, update, showall, exit\n"
          )


def run_console_ui():
    item_list = []
    print("Type a few commands separated by ';' then press ENTER")
    while True:
        commands_str = input(">>>")
        commands_str_lst = commands_str.split(';')
        for command in commands_str_lst:
            if command == 'exit':
                return 0
            else:
                args = command.split(',')
                if args[0] == "add":
                    item_list = validate_add(args, item_list)
                elif args[0] == "remove":
                    item_list = validate_remove(args, item_list)
                elif args[0] == "update":
                    item_list = validate_update(args, item_list)
                elif args[0] == "showall":
                    validate_showall(args, item_list)
                else:
                    print(f"'{args[0]}' is not a valid command!")
                    help_dialog()


def validate_add(args, item_list):
    if len(args) == 6:
        try:
            item_list = create(item_list, int(args[1]), args[2], args[3], float(args[4]), args[5])
        except ValueError:
            print("Argument for item ID should be a valid integer.\n"
                  "Argument for purchase price should be a valid float.")
    else:
        print("Command 'add' expects 5 arguments.")
    return item_list


def validate_update(args, item_list):
    if len(args) == 6:
        try:
            item_list = update(item_list, create_item(int(args[1]), args[2], args[3], float(args[4]), args[5]))
        except ValueError:
            print("Argument for item ID should be a valid integer.\n"
                  "Argument for purchase price should be a valid float.")
    else:
        print("Command 'update' expects 5 arguments.")
    return item_list


def validate_remove(args, item_list):
    if len(args) == 2:
        try:
            item_list = delete(item_list, int(args[1]))
        except ValueError:
            print("Argument for item ID should be a valid integer.")
    else:
        print("Command 'remove' expects a single argument.")
    return item_list


def validate_showall(args, item_list):
    if len(args) == 1:
        for item in item_list:
            print(get_str(item))
    else:
        print("Command 'showall' expects no arguments.")
