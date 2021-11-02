from Logic.total_worth_in_location import sum_of_all_prices_in_a_place
from Tests.test_crud import get_data


def test_sum_of_all_prices_in_a_place():
    items = get_data()
    assert sum_of_all_prices_in_a_place(items, "hall") == 2987.6


def test_total_worth_in_location():
    test_sum_of_all_prices_in_a_place()
