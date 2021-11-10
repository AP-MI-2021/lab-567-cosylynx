from Domain.item import create_item, get_id
from Logic.crud import create, update, delete, read


def get_data():
    return [
        create_item(1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'offc'),
        create_item(2, 'espressor', 'Espressor automat Philips EP3243/50', 2899.90, 'hall'),
        create_item(3, 'scaun', 'Scaun de birou ergonomic Kring Fit', 629.99, 'offc'),
        create_item(4, 'bec', 'Tub neon LED T5 90cm, Putere 15w', 27.80, 'hall'),
        create_item(5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'offc'),
        create_item(6, 'tablou', 'Tablou Canvas - Flori, Magnolia, 80 x 120 cm', 59.90, 'hall'),
        create_item(7, 'telefon', 'Telefon fix analogic Panasonic KX-TS520FXB', 86.87, 'entr')
    ]


def test_create():
    items = get_data()
    params = (100, 'new obj', 'new desc', 99.99, 'home', [], [])
    o_new = create_item(*params[:-2])
    new_items = create(items, *params)
    assert len(new_items) == len(items) + 1
    assert o_new in new_items


def test_read():
    items = get_data()
    some_o = items[3]
    assert read(items, get_id(some_o)) == some_o
    assert read(items, None) == items


def test_update():
    items = get_data()
    o_updated = create_item(2, "new obj", "nice obj", 100.00, "eBay")
    updated = update(items, o_updated, [], [])
    assert o_updated in updated
    assert o_updated not in items
    assert len(items) == len(updated)


def test_delete():
    items = get_data()
    to_delete = 2
    o_deleted = read(items, to_delete)
    deleted = delete(items, to_delete, [], [])
    assert o_deleted not in deleted
    assert o_deleted in items
    assert len(deleted) == len(items) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
