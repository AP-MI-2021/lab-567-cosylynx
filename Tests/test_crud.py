from Domain.object import create_object, get_id
from Logic.crud import create, update, delete, read


def get_data():
    return [
        create_object(1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'offc'),
        create_object(2, 'espressor', 'Espressor automat Philips EP3243/50', 2899.90, 'hall'),
        create_object(3, 'scaun', 'Scaun de birou ergonomic Kring Fit', 629.99, 'offc'),
        create_object(4, 'bec', 'Tub neon LED T5 90cm, Putere 15w', 27.80, 'hall'),
        create_object(5, 'cană', 'Cana pisica Abby ceramica 350ml', 59.90, 'offc'),
        create_object(6, 'tablou', 'Tablou Canvas - Flori, Magnolia, 80 x 120 cm', 59.90, 'hall'),
        create_object(7, 'telefon', 'Telefon fix analogic Panasonic KX-TS520FXB', 86.87, 'entr')
    ]


def test_create():
    objects = get_data()
    params = (100, 'new obj', 'new desc', 99.99, 'home')
    o_new = create_object(*params)
    new_objects = create(objects, *params)
    assert len(new_objects) == len(objects) + 1
    assert o_new in new_objects


def test_read():
    objects = get_data()
    some_o = objects[3]
    assert read(objects, get_id(some_o)) == some_o
    assert read(objects, None) == objects


def test_update():
    objects = get_data()
    o_updated = create_object(2, "new obj", "nice obj", 100.00, "eBay")
    updated = update(objects, o_updated)
    assert o_updated in updated
    assert o_updated not in objects
    assert len(objects) == len(updated)


def test_delete():
    objects = get_data()
    to_delete = 2
    o_deleted = read(objects, to_delete)
    deleted = delete(objects, to_delete)
    assert o_deleted not in deleted
    assert o_deleted in objects
    assert len(deleted) == len(objects) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
