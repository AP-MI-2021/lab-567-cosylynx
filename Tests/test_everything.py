from Tests.test_add_string_to_description import test_add_string_to_description
from Tests.test_crud import test_crud
from Tests.test_most_expensive_from_location import test_most_expensive_from_location
from Tests.test_move_items import test_move_items


def test_everything():
    test_crud()
    test_move_items()
    test_add_string_to_description()
    test_most_expensive_from_location()
