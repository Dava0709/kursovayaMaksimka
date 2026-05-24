from abc import ABC, abstractmethod

from models.delivery_result import DeliveryResult
from models.order import Order


class DeliveryAdapter(ABC):
    """Целевой интерфейс, который использует приложение FoodAdapter."""

    @abstractmethod
    def deliver_order(self, order: Order) -> DeliveryResult:
        pass
