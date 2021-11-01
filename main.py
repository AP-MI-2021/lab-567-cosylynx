from Tests.test_crud import test_crud
from Tests.test_functionality import test_functionalities
from UserInterface.console import run_main_ui


def main():
    run_main_ui()


if __name__ == '__main__':
    test_crud()
    test_functionalities()
    main()
