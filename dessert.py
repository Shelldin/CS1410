from abc import ABC, abstractmethod
from packaging import Packaging
from payable import Payable, PayType
from combine import Combinable


class DessertItem(ABC, Packaging):
    def __init__(self, name="", tax_percent=7.25):
        self.name = name
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return round(((self.calculate_cost() * self.tax_percent) / 100), 2)

    def __eq__(self, other):
        return self.calculate_cost() == other.calculate_cost()

    def __ne__(self, other):
        return self.calculate_cost() != other.calculate_cost()

    def __lt__(self, other):
        return self.calculate_cost() < other.calculate_cost()

    def __gt__(self, other):
        return self.calculate_cost() > other.calculate_cost()

    def __le__(self, other):
        return self.calculate_cost() <= other.calculate_cost()

    def __ge__(self, other):
        return self.calculate_cost() >= other.calculate_cost()


class Candy(DessertItem):
    def __init__(self, name='', candy_weight=0.0, price_per_pound=0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"

    def can_combine(self, other: "Combinable") -> bool:
        return (
            isinstance(other, Candy)
            and self.name == other.name
            and self.price_per_pound == other.price_per_pound
        )

    def combine(self, other: "Combinable") -> "Candy":
        if self.can_combine(other):
            self.candy_weight += other.candy_weight
        return self

    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)

    def __str__(self):
        return (f'{self.name} ({self.packaging}), {self.candy_weight}lbs, ${self.price_per_pound}/lb, '
                f'${self.calculate_cost()}, ${self.calculate_tax()}')


class Cookie(DessertItem):
    def __init__(self, name='', cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"

    def can_combine(self, other: "Combinable") -> bool:
        return (
                isinstance(other, Cookie)
                and self.name == other.name
                and self.price_per_dozen == other.price_per_dozen
        )

    def combine(self, other: "Combinable") -> "Cookie":
        if self.can_combine(other):
            self.cookie_quantity += other.cookie_quantity
        return self

    def __str__(self):
        return (f'{self.name} ({self.packaging}), {self.cookie_quantity} cookie(s), ${self.price_per_dozen}/dozen, '
                f'${self.calculate_cost()}, ${self.calculate_tax()}')

    def calculate_cost(self):
        return round((self.cookie_quantity / 12) * self.price_per_dozen, 2)


class IceCream(DessertItem):
    def __init__(self, name='', scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"

    def __str__(self):
        return (f'{self.name} ({self.packaging}), {self.scoop_count} scoop(s), ${self.price_per_scoop}/scoop, '
                f'${self.calculate_cost()}, ${self.calculate_tax()}')

    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)


class Sundae(IceCream):
    def __init__(self, name='', scoop_count=0, price_per_scoop=0.0,
                 topping_name='', topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"

    def __str__(self):
        return (f'{self.name} ({self.packaging}), {self.scoop_count} scoop(s), ${self.price_per_scoop}/scoop, '
                f'{self.topping_name} for ${self.topping_price}, '
                f'${self.calculate_cost()}, ${self.calculate_tax()}')

    def calculate_cost(self):
        return round(super().calculate_cost() + self.topping_price, 2)


class Order:
    def __init__(self):
        self.order = []
        self.payment_method = PayType.CASH

    def __str__(self):
        receipt_info = []
        for item in self.order:
            receipt_info.append(str(item))
        receipt_info.append(f"subtotal: {self.order_cost()}")
        receipt_info.append(f"total tax: {self.order_tax()}")
        receipt_info.append(f"Total: {round((self.order_cost() + self.order_tax()), 2)}")
        receipt_info.append(f"Paid with: {self.get_pay_type().name}")
        return "\n".join(receipt_info)

    def add(self, dessert_item):
        if not isinstance(dessert_item, Combinable):
            self.order.append(dessert_item)
        else:
            combined = False
            for item in self.order:
                if isinstance(item, Combinable) and item.can_combine(dessert_item):
                    item.combine(dessert_item)
                    combined = True
                    break
            if not combined:
                self.order.append(dessert_item)

    def __len__(self):
        return len(self.order)

    def order_cost(self):
        total_cost = 0
        for dessert_item in self.order:
            total_cost += dessert_item.calculate_cost()
        return round(total_cost, 2)

    def order_tax(self):
        total_tax = 0
        for dessert_item in self.order:
            total_tax += dessert_item.calculate_tax()
        return round(total_tax, 2)

    def sort(self):
        self.order.sort()

    def get_pay_type(self) -> PayType:
        if not isinstance(self.payment_method, PayType):
            raise ValueError(f"Invalid form of payment: {self.payment_method}")
        else:
            return self.payment_method

    def set_pay_type(self, payment_method: PayType) -> None:
        if not isinstance(payment_method, PayType):
            raise ValueError(f"Invalid form of payment: {payment_method}")
        self.payment_method = payment_method
