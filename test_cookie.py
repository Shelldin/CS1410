import pytest
from dessert import Cookie


def test_cookie():
    cookie = Cookie("Monster Cookie", 24, 6.0)
    assert cookie.name == "Monster Cookie"
    assert cookie.cookie_quantity == 24
    assert cookie.price_per_dozen == 6.0

    assert cookie.calculate_cost() == 12
    assert cookie.calculate_tax() == 0.87

    assert cookie.packaging == "Box"


def test_can_combine_same_candy():
    candy1 = Cookie('sugar', 0.5, 0.25)
    candy2 = Cookie('sugar', 1.25, 0.25)
    assert candy1.can_combine(candy2) == True

def test_can_combine_different_candy():
    candy1 = Cookie('sugar', 0.5, 0.25)
    candy2 = Cookie('peanut', 1.25, 0.25)
    assert candy1.can_combine(candy2) == False

def test_combine_candy():
    candy1 = Cookie('sugar', 3, 5.25)
    candy2 = Cookie('sugar', 4, 5.25)
    combined = candy1.combine(candy2)
    assert combined.cookie_quantity == 7