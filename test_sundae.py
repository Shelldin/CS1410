import pytest
from dessert import Sundae


def test_sundae():
    sundae = Sundae("Chocolate", 5, 1.25,
                    "Sprinkles", 0.25)
    assert sundae.name == "Chocolate"
    assert sundae.scoop_count == 5
    assert sundae.price_per_scoop == 1.25
    assert sundae.topping_name == "Sprinkles"
    assert sundae.topping_price == 0.25

    assert sundae.calculate_cost() == 6.5
    assert sundae.calculate_tax() == .47

    assert sundae.packaging == "Boat"
