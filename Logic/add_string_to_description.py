from copy import deepcopy

from Domain.item import get_pur_price


def append_str_to_price_above(items: list[list], threshold_price, string_to_description: str, undo, redo):
    """
    Adds a string to the end of items' descriptions if their price is greater than a given one

    :param items: the list of all items
    :param threshold_price: the price above which the string is added to description
    :param string_to_description: the string to be added to description
    :return: the list of items now each eligible item having their description modified
    :param undo:
    :param redo:
    """
    undo.append(deepcopy(items))
    redo.clear()
    for item in items:
        if get_pur_price(item) >= threshold_price:
            item[2] += ' ' + string_to_description
    return items
