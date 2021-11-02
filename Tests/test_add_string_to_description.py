from Logic.add_string_to_description import append_str_to_price_above
from Tests.test_crud import get_data


def test_append_str_to_price_above():
    items = get_data()
    assert append_str_to_price_above(items, 200, "- check integrity") == [
        [1, 'monitor', 'Monitor LED IPS Dell 27 in - check integrity', 899.90, 'offc'],
        [2, 'espressor', 'Espressor automat Philips EP3243/50 - check integrity', 2899.90, 'hall'],
        [3, 'scaun', 'Scaun de birou ergonomic Kring Fit - check integrity', 629.99, 'offc'],
        [4, 'bec', 'Tub neon LED T5 90cm, Putere 15w', 27.80, 'hall'],
        [5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'offc'],
        [6, 'tablou', 'Tablou Canvas - Flori, Magnolia, 80 x 120 cm', 59.90, 'hall'],
        [7, 'telefon', 'Telefon fix analogic Panasonic KX-TS520FXB', 86.87, 'entr']
    ]


def test_add_string_to_description():
    test_append_str_to_price_above()

