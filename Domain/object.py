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
    return {
        'obj_id': object_id,
        'name': name,
        'desc': description,
        'pur_price': purchase_price,
        'loc': location
    }


def get_id(object):
    """
    Getter for the object ID.
    :param object: an object
    :return: the object ID given as a parameter
    """
    return object['obj_id']


def get_name(object):
    """
    Getter for the object name.
    :param object: object
    :return: the object name given as a parameter
    """
    return object['name']


def get_desc(object):
    """
    Getter for the object description.
    :param object: object
    :return: the object description given as a parameter
    """
    return object['desc']


def get_pur_price(object):
    """
    Getter for the purchase price of the object.
    :param object: object
    :return: the object purchase price given as a parameter
    """
    return object['pur_price']


def get_loc(object):
    """
    Getter for the object current location.
    :param object: the object
    :return: the current object location given as a parameter
    """
    return object['loc']


def get_str(object):
    return f"The object called {get_name(object)} with id {get_id(object)} located at {get_loc(object)} purchased " \
           f"at price {get_pur_price(object)} and the following description: {get_desc(object)}"

