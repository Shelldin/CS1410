from typing import Protocol
from typing_extensions import runtime_checkable


@runtime_checkable
class Combinable(Protocol):
    def can_combine(self, other: "Combinable") -> bool:
        ...

    def combine(self, other: "Combinable") -> "Combinable":
        ...