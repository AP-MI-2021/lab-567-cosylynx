from copy import deepcopy

from Domain.item import get_loc, get_id


def get_from_location(items, location: str):
    """
    Creates a list with all items that are at the location the user provided
    :param location:  the location the user wants to move items from
    :param items: the list with items
    :return: a list with the items that are at the location
    """
    in_location = []
    for item in items:
        if get_loc(item) == location:
            in_location.append(item)
    return in_location


def locations_list(items):
    """
    Creates a list with all locations where items are
    :param items: a list with all items
    :return: a list with only the locations of those item (each location appears only once)
    """
    locations = []
    for item in items:
        if get_loc(item) not in locations:
            locations.append(get_loc(item))
    return locations


def update_items_location(items, location_from: str, location_to: str, undo, redo):
    """
    Moves items from one location to the other.
    :param redo:
    :param undo:
    :param items: the list of all items
    :param location_from: the location from where items are moved
    :param location_to: the location to where items are moved
    :return: a list of items with the new location
    """
    if location_from not in locations_list(items):
        raise ValueError('The move-from location must be chosen from the list above!')
    if len(location_to) > 4:
        raise ValueError(f"The new location must have 4 characters at most!")
    undo.append(deepcopy(items))
    redo.clear()
    for obj_from_loc in get_from_location(items, location_from):
        for item in items:
            if get_id(obj_from_loc) == get_id(item):
                item[4] = location_to
    return items
