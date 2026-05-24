from adapters.base import DeliveryAdapter
from models.delivery_result import DeliveryResult
from models.order import Order
from services.delivery_services import YandexDeliveryService


class YandexAdapter(DeliveryAdapter):
    def __init__(self, service: YandexDeliveryService):
        self.service = service

    def deliver_order(self, order: Order) -> DeliveryResult:
        service_message = self.service.start_yandex_shipping(order)
        return DeliveryResult(
            adapter_name="YandexAdapter",
            messages=[
                "Используется YandexAdapter...",
                "Заказ успешно адаптирован.",
                service_message,
            ],
        )
