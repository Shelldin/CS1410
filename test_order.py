import pytest
from dessert import Candy, Cookie, IceCream, Sundae, Order
from payable import PayType


def test_default_payment_type():
    order = Order()
    assert order.get_pay_type() == PayType.CASH


def test_set_payment_type_cash():
    order = Order()
    order.set_pay_type(PayType.CASH)
    assert order.get_pay_type() == PayType.CASH


def test_set_payment_type_card():
    order = Order()
    order.set_pay_type(PayType.CARD)
    assert order.get_pay_type() == PayType.CARD


def test_set_payment_type_phone():
    order = Order()
    order.set_pay_type(PayType.PHONE)
    assert order.get_pay_type() == PayType.PHONE


def test_set_invalid_payment_type():
    order = Order()
    with pytest.raises(ValueError):
        order.set_pay_type("Invalid payment method")


def test_get_invalid_payment_type():
    order = Order()
    with pytest.raises(ValueError):
        order.payment_method = "Invalid payment method"
        order.get_pay_type()


def test_order_sort():
    order = Order()
    item1 = Candy('Candy Corn', 1.5, .25)  # Cost: 0.375
    item2 = Cookie("Chocolate Chip", 6, 3.99)  # Cost: 1.995
    item3 = IceCream("Pistachio", 2, .79)  # Cost: 1.58
    item4 = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)  # Cost: 3.36
    item5 = Candy("Gummy Bears", .25, .35)  # Cost: 0.0875

    order.add(item1)
    order.add(item2)
    order.add(item3)
    order.add(item4)
    order.add(item5)

    order.sort()

    sorted_items = [item5, item1, item3, item2, item4]

    assert order.order == sorted_items
