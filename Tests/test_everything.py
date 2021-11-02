from Tests.test_add_string_to_description import test_add_string_to_description
from Tests.test_crud import test_crud
from Tests.test_move_objects import test_move_objects


def test_everything():
    test_crud()
    test_move_objects()
    test_add_string_to_description()