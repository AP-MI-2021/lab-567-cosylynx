from Domain.object import get_loc, get_id


def get_from_location(objects, location: str):
    """
    Creates a list with all objects that are at the location the user provided
    :param location:  the location the user wants to move objects from
    :param objects: the list with objects
    :return: a list with the objects that are at the location
    """
    in_location = []
    for object in objects:
        if get_loc(object) == location:
            in_location.append(object)
    return in_location


def locations_list(objects):
    """
    Creates a list with all locations where objects are
    :param objects: a list with all objects
    :return: a list with only the locations of those object (each location appears only once)
    """
    locations = []
    for object in objects:
        if get_loc(object) not in locations:
            locations.append(get_loc(object))
    return locations


def update_objects_location(objects, location_from: str, location_to: str):
    """
    Moves objects from one location to the other.
    :param objects: the list of all objects
    :param location_from: the location from where objects are moved
    :param location_to: the location to where objects are moved
    :return: a list of objects with the new location
    """
    for obj_from_loc in get_from_location(objects, location_from):
        for object in objects:
            if get_id(obj_from_loc) == get_id(object):
                object[4] = location_to
    return objects
