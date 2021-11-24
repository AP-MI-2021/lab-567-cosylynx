from Logic.add_string_to_description import append_str_to_price_above
from Logic.crud import create, update, delete
from Logic.move_items import update_items_location
from Logic.order_ascending_price import order_ascending_by_price
from Logic.undo_redo import do_undo, do_redo
from Tests.test_crud import get_data


def test_undo_redo():
    items = get_data()
    undo = []
    redo = []

    # Test when creating a new object
    items = create(items, 19, "toy", "car", 29.9, "home", undo, redo)
    assert undo == [get_data()]
    do_undo(undo, redo, items)
    assert undo == []
    assert redo == [items]
    do_redo(undo, redo, items)
    assert redo == []

    # Test when updating an object
    undo.clear()
    redo.clear()
    new_item = [1, "soy", "bar", 99.2, "dome"]
    items = update(items, new_item, undo, redo)
    do_undo(undo, redo, items)
    assert undo == []
    assert redo == [items]
    do_redo(undo, redo, items)
    assert redo == []

    # Test when deleting an object
    undo.clear()
    redo.clear()
    items = delete(items, 2, undo, redo)
    do_undo(undo, redo, items)
    assert undo == []
    assert redo == [items]
    do_redo(undo, redo, items)
    assert redo == []

    # Test when moving objects from one place to another
    undo.clear()
    redo.clear()
    items = update_items_location(items, "offc", "home", undo, redo)
    assert items not in undo
    do_undo(undo, redo, items)
    assert undo == []
    assert redo == [items]
    do_redo(undo, redo, items)
    assert redo == []

    # Test when adding string to description
    undo.clear()
    redo.clear()
    items = append_str_to_price_above(items, 50, "more than fifty", undo, redo)
    assert items not in undo
    do_undo(undo, redo, items)
    assert undo == []
    assert redo == [items]
    do_redo(undo, redo, items)
    assert redo == []

    # Test when ordering items
    undo.clear()
    redo.clear()
    items = order_ascending_by_price(items, undo, redo)
    assert items not in undo
    do_undo(undo, redo, items)
    assert undo == []
    assert redo == [items]
    do_redo(undo, redo, items)
    assert redo == []
