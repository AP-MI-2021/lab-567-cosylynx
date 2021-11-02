from Domain.object import get_pur_price


def append_str_to_price_above(objects: list[list], threshold_price: int, string_to_description: str):
    """
    Adds a string to the end of objects' descriptions if their price is greater than a given one
    :param objects: the list of all objects
    :param threshold_price: the price above which the string is added to description
    :param string_to_description: the string to be added to description
    :return: the list of objects now each eligible object having their description modified
    """
    for object in objects:
        if get_pur_price(object) >= threshold_price:
            object[2] += ' ' + string_to_description
    return objects