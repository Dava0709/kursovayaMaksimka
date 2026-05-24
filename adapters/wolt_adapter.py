from adapters.base import DeliveryAdapter
from models.delivery_result import DeliveryResult
from models.order import Order
from services.delivery_services import WoltService


class WoltAdapter(DeliveryAdapter):
    def __init__(self, service: WoltService):
        self.service = service

    def deliver_order(self, order: Order) -> DeliveryResult:
        service_message = self.service.create_wolt_delivery(order)
        return DeliveryResult(
            adapter_name="WoltAdapter",
            messages=[
                "Используется WoltAdapter...",
                "Заказ успешно адаптирован.",
                service_message,
            ],
        )
