from Logic.move_items import get_from_location, locations_list, update_items_location
from Tests.test_crud import get_data


def test_get_from_location():
    items = get_data()
    assert get_from_location(items, "offc") == [
        [1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'offc'],
        [3, 'scaun', 'Scaun de birou ergonomic Kring Fit', 629.99, 'offc'],
        [5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'offc']
    ]


def test_locations_list():
    items = get_data()
    assert locations_list(items) == ["offc", "hall", "entr"]


def test_update_items_location():
    items = get_data()
    assert update_items_location(items, "offc", "home", [], []) == [
        [1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'home'],
        [2, 'espressor', 'Espressor automat Philips EP3243/50', 2899.90, 'hall'],
        [3, 'scaun', 'Scaun de birou ergonomic Kring Fit', 629.99, 'home'],
        [4, 'bec', 'Tub neon LED T5 90cm, Putere 15w', 27.80, 'hall'],
        [5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'home'],
        [6, 'tablou', 'Tablou Canvas - Flori, Magnolia, 80 x 120 cm', 59.90, 'hall'],
        [7, 'telefon', 'Telefon fix analogic Panasonic KX-TS520FXB', 86.87, 'entr']
    ]


def test_move_items():
    test_get_from_location()
    test_locations_list()
    test_update_items_location()
