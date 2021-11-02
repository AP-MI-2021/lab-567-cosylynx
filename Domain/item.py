def create_item(item_id: int, name: str, description: str, purchase_price: float, location: str):
    """
    Create an item.
    :param item_id: the ID of the item, it has to be unique
    :param name: the name of the item
    :param description: a description of the item
    :param purchase_price: the price the item had when it was purchased
    :param location: the purchase place of the item
    :return: an item
    """
    return [item_id, name, description, purchase_price, location]


def get_id(item):
    """
    Getter for the item ID.
    :param item: an item
    :return: the item ID given as a parameter
    """
    return item[0]


def get_name(item):
    """
    Getter for the item name.
    :param item: item
    :return: the item name given as a parameter
    """
    return item[1]


def get_desc(item):
    """
    Getter for the item description.
    :param item: item
    :return: the item description given as a parameter
    """
    return item[2]


def get_pur_price(item):
    """
    Getter for the purchase price of the item.
    :param item: item
    :return: the item purchase price given as a parameter
    """
    return item[3]


def get_loc(item):
    """
    Getter for the item current location.
    :param item: the item
    :return: the current item location given as a parameter
    """
    return item[4]


def get_str(item):
    return f"item with ID: {get_id(item)}, name: {get_name(item)}, description: {get_desc(item)}, " \
           f"purchase price: {get_pur_price(item)} and location: {get_loc(item)}"
