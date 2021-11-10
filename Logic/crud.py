from Domain.item import create_item, get_id


def create(items_lst, item_id: int, name, description, purchase_price, location, undo, redo):
    """
    Creates a new item.
    :param items_lst: a list containing created items
    :param item_id: the ID of the item, it has to be unique
    :param name: the name of the item
    :param description: a description of the item
    :param purchase_price: the price the item had when it was purchased
    :param undo:
    :param redo:
    :param location: the current place of the item
    :return: a new list containing items_lst and the newly created item
    """
    if read(items_lst, item_id) is not None:
        raise ValueError(f"An item with id {item_id} already exists.")
    item = create_item(item_id, name, description, purchase_price, location)
    undo.append(items_lst)
    redo.clear()
    return items_lst + [item]


def read(items_lst, item_id: int = None):
    """
    Reads an item from the available list.
    :param items_lst: a list containing items
    :param item_id: the ID of the item
    :return: the item with ID item_id, or the whole item list if item_id = None
    """
    if not item_id:
        return items_lst
    item_with_id = None
    for item in items_lst:
        if get_id(item) == item_id:
            item_with_id = item
    if item_with_id:
        return item_with_id
    return None


def update(items_lst, new_item, undo, redo):
    """
    Update an item.
    :param redo:
    :param undo:
    :param items_lst: the list of items
    :param new_item: the item from the list that will update - id must be existent
    :return: a list with the updated item
    """
    if read(items_lst, get_id(new_item)) is None:
        raise ValueError(f"There is no item with id {get_id(new_item)} that can be updated.")
    new_items = []
    for item in items_lst:
        if get_id(item) != get_id(new_item):
            new_items.append(item)
        else:
            new_items.append(new_item)
    undo.append(items_lst)
    redo.clear()
    return new_items


def delete(items_lst, item_id, undo, redo):
    """
    Delete an item from the item list.
    :param redo:
    :param undo:
    :param items_lst: the list of items
    :param item_id: the ID of the item
    :return: a list of items without the one select for deletion
    """
    new_items = []
    for item in items_lst:
        if get_id(item) != item_id:
            new_items.append(item)
    undo.append(items_lst)
    redo.clear()
    return new_items
