from Domain.item import get_str
from Logic.add_string_to_description import append_str_to_price_above
from Logic.crud import *
from Logic.most_expensive_from_location import get_highest_price_at_location
from Logic.move_items import locations_list, update_items_location
from Logic.order_ascending_price import order_ascending_by_price
from Logic.total_worth_in_location import sum_of_all_prices_in_a_place
from Logic.undo_redo import do_undo, do_redo


# CRUD related functionalities
def handle_show_all(items):
    if not items:
        print("There are currently no objects in the inventory!")
    for item in items:
        print(get_str(item))


def handle_add(item_list, undo, redo):
    obj_id = int(input("Enter item ID: "))
    obj_name = input("Enter item name: ")
    obj_desc = input("Enter item description: ")
    obj_pur_price = float(input("Enter item purchase price: "))
    obj_location = input("Enter item location: ")
    return create(item_list, obj_id, obj_name, obj_desc, obj_pur_price, obj_location, undo, redo)


def handle_change(item_list, undo, redo):
    to_be_changed_id = int(input("Enter the item's ID you'd like to change: "))
    to_be_changed_name = input("Enter the item's new name: ")
    to_be_changed_desc = input("Enter the item's new description: ")
    to_be_changed_pur_price = float(input("Enter the item's new purchase price: "))
    to_be_changed_loc = input("Enter the item's new item location: ")
    new_item = create_item(to_be_changed_id, to_be_changed_name, to_be_changed_desc,
                           to_be_changed_pur_price, to_be_changed_loc)
    return update(item_list, new_item, undo, redo)


def handle_delete(item_list, undo, redo):
    item_id = int(input("Enter item ID to be deleted: "))
    return delete(item_list, item_id, undo, redo)


# Extra functionalities
def handle_move(items, undo, redo):
    if not items:
        raise ValueError('There are no items in the inventory')
    print(f"Used locations are: {locations_list(items)}.")
    move_from = input("Enter the location from which you wish to move all items: ")
    move_to = input("Enter the location where you want the items to be moved: ")
    return update_items_location(items, move_from, move_to, undo, redo)


def handle_add_str_do_description(items, undo, redo):
    if not items:
        raise ValueError('There are no items in the inventory')
    try:
        threshold_price = int(input("Enter the minimum price of items whose description will be modified: "))
    except ValueError:
        print("The value of the price must be an integer!")
        return
    add_string = input("Now enter a string to add to the end of their descriptions: ")
    return append_str_to_price_above(items, threshold_price, add_string, undo, redo)


def handle_max_price_in_location(items):
    if not items:
        raise ValueError('There are no items in the inventory')
    print(f"Used locations are: {locations_list(items)}.")
    from_location = input("Enter the location where you want to see the most expensive item/items: ")
    print("Most expensive item/items from this location are: ")
    for item in get_highest_price_at_location(items, from_location):
        print(item)


def handle_order_ascending(items, undo, redo):
    if not items:
        raise ValueError('There are no items in the inventory')
    print("The items have been ordered!")
    return order_ascending_by_price(items, undo, redo)


def handle_total_worth(items):
    if not items:
        raise ValueError('There are no items in the inventory')
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
