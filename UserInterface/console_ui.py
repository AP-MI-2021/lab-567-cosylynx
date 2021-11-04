from Logic.crud import create


def run_console_ui(items):
    while True:
        commands = input('Type some commands: ')
        if commands == "help":
            help_dialog()
        else:
            commands_lst = commands.split(";")
            for i in range(len(commands_lst)):
                console_command = commands_lst[i].split(",")
                if commands_lst[0] == "exit":
                elif console_command[0] == "add":
                    try:
                        items = create(console_command[1], console_command[2], console_command[3],
                                            console_command[4], console_command[5])
                    except ValueError as ve:
                        print("Eroare : {}".format(ve))
                elif optiuni[0] == "Showall":
                    handle_show_all(items)
                elif optiuni[0] == "Update":
                    lista = modifica_rezervare(optiuni[1], optiuni[2], optiuni[3], optiuni[4], optiuni[5], lista)
                elif optiuni[0] == "exit":
                    try:
                        lista = sterge_rezervare(optiuni[1], lista)
                    except ValueError as ve1:
                        print("Eroare : {}".format(ve1))
                else:
                    print("Optiune gresita! Acceseaza comanda 'help'!")

"""
def help_dialog():
    print("Usage: \n"
          "add,<id>,<name>,<description>,<purchase_price>,<location>;\n"
          "remove,<id>;\n"
          "update,<id>,<name>,<description>,<purchase_price>,<location>;\n"
          "showall;\n"
          "exit;\n"
          "Use ',' to separate the arguments of a command and ';' to mark the end of the command.\n"
          " \n"
          "Available commands are:\n"
          "add, remove, update, showall, exit\n"
          )

help_dialog()