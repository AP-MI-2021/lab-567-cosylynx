from Logic.order_ascending_price import order_ascending_by_price
from Tests.test_crud import get_data


def test_order_ascending_by_price():
    items = get_data()
    undo = []
    redo = []
    assert order_ascending_by_price(items, undo, redo) == [
        [4, 'bec', 'Tub neon LED T5 90cm, Putere 15w', 27.80, 'hall'],
        [5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'offc'],
        [6, 'tablou', 'Tablou Canvas - Flori, Magnolia, 80 x 120 cm', 59.90, 'hall'],
        [7, 'telefon', 'Telefon fix analogic Panasonic KX-TS520FXB', 86.87, 'entr'],
        [3, 'scaun', 'Scaun de birou ergonomic Kring Fit', 629.99, 'offc'],
        [1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'offc'],
        [2, 'espressor', 'Espressor automat Philips EP3243/50', 2899.90, 'hall']
    ]


def test_order_ascending_price():
    test_order_ascending_by_price()
