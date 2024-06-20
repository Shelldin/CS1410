import pytest
from dessert import Candy


def test_candy():
    candy = Candy("Toffifay", .5, 1.5)
    assert candy.name == "Toffifay"
    assert candy.candy_weight == .5
    assert candy.price_per_pound == 1.5

    assert candy.calculate_cost() == .75
    assert candy.calculate_tax() == 0.05

    assert candy.packaging == "Bag"


def test_can_combine_same_candy():
    candy1 = Candy('Gummy Bears', 0.5, 0.25)
    candy2 = Candy('Gummy Bears', 1.25, 0.25)
    assert candy1.can_combine(candy2) == True


def test_can_combine_different_candy():
    candy1 = Candy('Gummy Bears', 0.5, 0.25)
    candy2 = Candy('Sour Worms', 1.25, 0.25)
    assert candy1.can_combine(candy2) == False


def test_combine_candy():
    candy1 = Candy('Gummy Bears', 0.5, 0.25)
    candy2 = Candy('Gummy Bears', 1.25, 0.25)
    combined = candy1.combine(candy2)
    assert combined.candy_weight == 1.75
