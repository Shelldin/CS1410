import pytest
from dessertshop import Customer
from dessert import Order


def test_unique_customer_ids():
    customer1 = Customer('Willy Wonka')
    customer2 = Customer('Grandpa Joe')
    customer3 = Customer('Charlie')
    assert customer1.customer_id != customer2.customer_id
    assert customer1.customer_id != customer3.customer_id
    assert customer2.customer_id != customer3.customer_id
    assert customer1.customer_id == 1
    assert customer2.customer_id == 2
    assert customer3.customer_id == 3


def test_customer_creation():
    customer = Customer('Slugworth')
    assert customer.customer_name == 'Slugworth'
    assert customer.order_history == []
    assert customer.customer_id == 4


def test_add2history():
    customer = Customer('Augustus Gloop')
    order = Order()
    customer.add2history(order)
    assert len(customer.order_history) == 1
    assert customer.order_history[0] == order
