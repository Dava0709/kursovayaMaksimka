from dataclasses import dataclass
from typing import List


@dataclass
class OrderItem:
    name: str
    quantity: int
    price: int


@dataclass
class Order:
    customer_name: str
    address: str
    items: List[OrderItem]
    total: int

    def summary(self) -> str:
        products = ", ".join(f"{item.quantity}x {item.name}" for item in self.items)
        return f"{products}. Итого: {self.total} тг. Адрес: {self.address}"
