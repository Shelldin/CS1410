from typing import Protocol
from enum import Enum, auto


class PayType(Enum):
    CASH = auto()
    CARD = auto()
    PHONE = auto()


class Payable(Protocol):
    payment_method = PayType.CASH
    def get_pay_type(self) -> PayType:
        if not isinstance(self.payment_method, PayType):
            raise ValueError(f"Invalid form of payment: {self.payment_method}")
        else:
            return self.payment_method

    def set_pay_type(self, payment_method: PayType) -> None:
        if payment_method not in PayType:
            raise ValueError("Invalid payment method")