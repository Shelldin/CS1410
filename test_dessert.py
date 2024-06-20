import pytest
from dessert import Candy


def test_dessert_item():
    dessert_item = Candy('Test Dessert', 0, 0)
    assert dessert_item.name == 'Test Dessert'
    assert dessert_item.tax_percent == 7.25
    assert dessert_item.packaging == "Bag"


def test_eq():
    item1 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    item2 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    assert item1 == item2


def test_ne():
    item1 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    item2 = Candy('Gummy Bears', .25, .35)  # Cost: 0.0875
    assert item1 != item2


def test_lt():
    item1 = Candy('Gummy Bears', .25, .35)  # Cost: 0.0875
    item2 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    assert item1 < item2


def test_gt():
    item1 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    item2 = Candy('Gummy Bears', .25, .35)  # Cost: 0.0875
    assert item1 > item2


def test_le():
    item1 = Candy('Gummy Bears', .25, .35)  # Cost: 0.0875
    item2 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    item3 = Candy('Gummy Bears', .25, .35)  # Cost: 0.0875
    assert item1 <= item2
    assert item1 <= item3


def test_ge():
    item1 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    item2 = Candy('Gummy Bears', .25, .35)  # Cost: 0.0875
    item3 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    assert item1 >= item2
    assert item1 >= item3
