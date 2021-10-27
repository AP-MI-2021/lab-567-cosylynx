from Domain.object import create_object, get_id


def create(objects_lst, object_id: int, name, description, purchase_price, location):
    """
    Creates a new object.
    :param objects_lst: a list containing created objects
    :param object_id: the ID of the object, it has to be unique
    :param name: the name of the object
    :param description: a description of the object
    :param purchase_price: the price the object had when it was purchased
    :param location: the current place of the object
    :return: a new list containing objects_lst and the newly created object
    """
    object = create_object(object_id, name, description, purchase_price, location)
    return objects_lst + [object]


def read(objects_lst, object_id=None):
    """
    Reads an object from the available list.
    :param objects_lst: a list containing objects
    :param object_id: the ID of the object
    :return: the object with ID object_id, or the whole object list if object_id = None
    """
    object_with_id = None
    for object in objects_lst:
        if get_id(object) == object_id:
            object_with_id = object
    if object_with_id:
        return object_with_id
    return objects_lst


def update(objects_lst, new_object):
    """
    Update an object.
    :param objects_lst: the list of objects
    :param new_object: the object from the list that will update - id must be existent
    :return: a list with the updated object
    """
    new_objects = []
    for object in objects_lst:
        if get_id(object) != get_id(new_object):
            new_objects.append(object)
        else:
            new_objects.append(new_object)
    return new_objects


def delete(objects_lst, object_id):
    """
    Delete an object from the object list.
    :param objects_lst: the list of objects
    :param object_id: the ID of the object
    :return: a list of objects without the one select for deletion
    """
    new_objects = []
    for object in objects_lst:
        if get_id(object) != object_id:
            new_objects.append(object)
    return new_objects
