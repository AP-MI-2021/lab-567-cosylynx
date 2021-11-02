from Domain.item import get_pur_price
from Logic.move_items import get_from_location


def get_highest_price_at_location(items, location: str):
    """
    Determines the most expensive items from a given location.
    :param items: the list of all items
    :param location: the location from where the user needs the most expensive item
    :return: a list with the most expensive items(if more items have the same price)
    """
    max_price = 0
    items_with_max_price = []
    items_at_location = get_from_location(items, location)
    for item in items_at_location:
        if get_pur_price(item) > max_price:
            max_price = get_pur_price(item)
    for item in items_at_location:
        if get_pur_price(item) == max_price:
            items_with_max_price.append(item)
    return items_with_max_price
