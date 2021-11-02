from Logic.most_expensive_from_location import get_highest_price_at_location
from Tests.test_crud import get_data


def test_get_highest_price_at_location():
    items = get_data()
    assert get_highest_price_at_location(items, "offc") == [
        [1, 'monitor', 'Monitor LED IPS Dell 27 in', 899.90, 'offc']
    ]


def test_most_expensive_from_location():
    test_get_highest_price_at_location()
