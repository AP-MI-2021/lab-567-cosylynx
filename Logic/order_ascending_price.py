from operator import itemgetter


def order_ascending_by_price(items, undo, redo):
    """
    Orders the list of items in ascending order by purchase price
    :param redo:
    :param undo:
    :param items: the list of items
    :return: the ordered list
    """
    undo.append(deepcopy(items))
    redo.clear()
    items.sort(key=itemgetter(3))

    return items
