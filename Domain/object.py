def create_object(object_id: int, name, description, purchase_price, location):
    """
    Create an object.
    :param object_id: the ID of the object, it has to be unique
    :param name: the name of the object
    :param description: a description of the object
    :param purchase_price: the price the object had when it was purchased
    :param location: the purchase place of the object
    :return: an object
    """
    return [object_id, name, description, purchase_price, location]


def get_id(object):
    """
    Getter for the object ID.
    :param object: an object
    :return: the object ID given as a parameter
    """
    return object[0]


def get_name(object):
    """
    Getter for the object name.
    :param object: object
    :return: the object name given as a parameter
    """
    return object[1]


def get_desc(object):
    """
    Getter for the object description.
    :param object: object
    :return: the object description given as a parameter
    """
    return object[2]


def get_pur_price(object):
    """
    Getter for the purchase price of the object.
    :param object: object
    :return: the object purchase price given as a parameter
    """
    return object[3]


def get_loc(object):
    """
    Getter for the object current location.
    :param object: the object
    :return: the current object location given as a parameter
    """
    return object[4]


def get_str(object):
    return f"Object with ID: {get_id(object)}, name: {get_name(object)}, description: {get_desc(object)}, " \
           f"purchase price: {get_pur_price(object)} and location: {get_loc(object)}"
