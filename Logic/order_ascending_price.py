from operator import itemgetter


def order_ascending_by_price(items):
    """
    Orders the list of items in ascending order by purchase price
    :param items: the list of items
    :return: the ordered list
    """
    items.sort(key=itemgetter(3))
    print(items)
    return items
