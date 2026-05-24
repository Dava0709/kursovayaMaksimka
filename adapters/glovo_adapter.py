from adapters.base import DeliveryAdapter
from models.delivery_result import DeliveryResult
from models.order import Order
from services.delivery_services import GlovoService


class GlovoAdapter(DeliveryAdapter):
    def __init__(self, service: GlovoService):
        self.service = service

    def deliver_order(self, order: Order) -> DeliveryResult:
        service_message = self.service.send_glovo_package(order)
        return DeliveryResult(
            adapter_name="GlovoAdapter",
            messages=[
                "Используется GlovoAdapter...",
                "Заказ успешно адаптирован.",
                service_message,
            ],
        )
