from Logic.functionality import get_from_location, locations_list, update_objects_location, append_str_to_price_above
from Tests.test_crud import get_data


def test_get_from_location():
    objects = get_data()
    assert get_from_location(objects, "offc") == [
        [1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'offc'],
        [3, 'scaun', 'Scaun de birou ergonomic Kring Fit', 629.99, 'offc'],
        [5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'offc']
    ]


def test_locations_list():
    objects = get_data()
    assert locations_list(objects) == ["offc", "hall", "entr"]


def test_update_objects_location():
    objects = get_data()
    assert update_objects_location(objects, "offc", "home") == [
        [1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'home'],
        [2, 'espressor', 'Espressor automat Philips EP3243/50', 2899.90, 'hall'],
        [3, 'scaun', 'Scaun de birou ergonomic Kring Fit', 629.99, 'home'],
        [4, 'bec', 'Tub neon LED T5 90cm, Putere 15w', 27.80, 'hall'],
        [5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'home'],
        [6, 'tablou', 'Tablou Canvas - Flori, Magnolia, 80 x 120 cm', 59.90, 'hall'],
        [7, 'telefon', 'Telefon fix analogic Panasonic KX-TS520FXB', 86.87, 'entr']
    ]


def test_append_str_to_price_above():
    objects = get_data()
    assert append_str_to_price_above(objects, 200, "- check integrity") == [
        [1, 'monitor', 'Monitor LED IPS Dell 27 in - check integrity', 899.90, 'offc'],
        [2, 'espressor', 'Espressor automat Philips EP3243/50 - check integrity', 2899.90, 'hall'],
        [3, 'scaun', 'Scaun de birou ergonomic Kring Fit - check integrity', 629.99, 'offc'],
        [4, 'bec', 'Tub neon LED T5 90cm, Putere 15w', 27.80, 'hall'],
        [5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'offc'],
        [6, 'tablou', 'Tablou Canvas - Flori, Magnolia, 80 x 120 cm', 59.90, 'hall'],
        [7, 'telefon', 'Telefon fix analogic Panasonic KX-TS520FXB', 86.87, 'entr']
    ]


def test_functionalities():
    # Moving object from one location to another
    test_get_from_location()
    test_locations_list()
    test_update_objects_location()
    # Adding a string to the end of objects' descriptions if their price is greater than a given
    test_append_str_to_price_above()

