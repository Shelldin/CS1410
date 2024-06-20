import pytest
from dessert import IceCream


def test_ice_cream():
    ice_cream = IceCream("Cookies and Cream", 3, 1.5)
    assert ice_cream.name == "Cookies and Cream"
    assert ice_cream.scoop_count == 3
    assert ice_cream.price_per_scoop == 1.5

    assert ice_cream.calculate_cost() == 4.5
    assert ice_cream.calculate_tax() == 0.33

    assert ice_cream.packaging == "Bowl"
