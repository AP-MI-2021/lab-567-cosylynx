from Domain.item import get_pur_price
from Logic.move_items import get_from_location, locations_list


def sum_of_all_prices_in_a_place(items, location: str):
    """
    Calculates the sum of the purchase price from each item on a given location
    :param items: the list of items
    :param location: the location from where the user wishes to know the total worth
    :return: the total worth of the items on a particular location
    """
    if location not in locations_list(items):
        raise ValueError("The location entered is not in the list of used locations!")
    sum_of_prices = 0
    items_at_location = get_from_location(items, location)
    for item in items_at_location:
        sum_of_prices += get_pur_price(item)
    return round(sum_of_prices, 3)
