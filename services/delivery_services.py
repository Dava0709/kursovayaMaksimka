from models.order import Order


class GlovoService:
    """Сторонний сервис со своим несовместимым API."""

    def send_glovo_package(self, order: Order) -> str:
        return f"Отправляем заказ в систему Glovo: {order.summary()}"


class WoltService:
    """Сторонний сервис со своим несовместимым API."""

    def create_wolt_delivery(self, order: Order) -> str:
        return f"Создаем доставку в системе Wolt: {order.summary()}"


class YandexDeliveryService:
    """Сторонний сервис со своим несовместимым API."""

    def start_yandex_shipping(self, order: Order) -> str:
        return f"Запускаем доставку через Yandex Delivery: {order.summary()}"
