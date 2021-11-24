from Tests.test_add_string_to_description import test_add_string_to_description
from Tests.test_crud import test_crud
from Tests.test_most_expensive_from_location import test_most_expensive_from_location
from Tests.test_move_items import test_move_items
from Tests.test_order_ascending_price import test_order_ascending_price
from Tests.test_total_worth_in_location import test_total_worth_in_location
from Tests.test_undo_redo import test_undo_redo


def test_everything():
    test_crud()
    test_move_items()
    test_add_string_to_description()
    test_most_expensive_from_location()
    test_order_ascending_price()
    test_total_worth_in_location()
    test_undo_redo()
