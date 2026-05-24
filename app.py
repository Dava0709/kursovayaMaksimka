from flask import Flask, jsonify, render_template, request, session

from adapters.glovo_adapter import GlovoAdapter
from adapters.wolt_adapter import WoltAdapter
from adapters.yandex_adapter import YandexAdapter
from models.order import Order, OrderItem
from services.delivery_services import GlovoService, WoltService, YandexDeliveryService
from services.menu_service import get_categories, get_featured_restaurants, get_menu_items


app = Flask(__name__)
app.config["SECRET_KEY"] = "foodadapter-dev-secret"

DELIVERY_ADAPTERS = {
    "glovo": GlovoAdapter(GlovoService()),
    "wolt": WoltAdapter(WoltService()),
    "yandex": YandexAdapter(YandexDeliveryService()),
}


def get_cart() -> dict:
    return session.setdefault("cart", {})


def cart_payload() -> dict:
    menu_by_id = {item["id"]: item for item in get_menu_items()}
    items = []
    total = 0

    for item_id, quantity in get_cart().items():
        product = menu_by_id.get(item_id)
        if not product:
            continue

        subtotal = product["price"] * quantity
        total += subtotal
        items.append(
            {
                "id": item_id,
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity,
                "subtotal": subtotal,
                "image": product["image"],
            }
        )

    return {"items": items, "total": total, "count": sum(item["quantity"] for item in items)}


@app.route("/")
def index():
    return render_template(
        "index.html",
        categories=get_categories(),
        restaurants=get_featured_restaurants(),
        menu_items=get_menu_items(),
        cart=cart_payload(),
    )


@app.route("/cart")
def cart():
    return render_template("cart.html", cart=cart_payload())


@app.route("/api/cart", methods=["GET"])
def api_cart():
    return jsonify(cart_payload())


@app.route("/api/cart/add", methods=["POST"])
def add_to_cart():
    item_id = request.json.get("item_id")
    menu_ids = {item["id"] for item in get_menu_items()}

    if item_id not in menu_ids:
        return jsonify({"error": "Блюдо не найдено"}), 404

    cart = get_cart()
    cart[item_id] = cart.get(item_id, 0) + 1
    session.modified = True
    return jsonify(cart_payload())


@app.route("/api/cart/update", methods=["POST"])
def update_cart():
    item_id = request.json.get("item_id")
    quantity = int(request.json.get("quantity", 1))
    cart = get_cart()

    if quantity <= 0:
        cart.pop(item_id, None)
    else:
        cart[item_id] = quantity

    session.modified = True
    return jsonify(cart_payload())


@app.route("/api/cart/remove", methods=["POST"])
def remove_from_cart():
    item_id = request.json.get("item_id")
    get_cart().pop(item_id, None)
    session.modified = True
    return jsonify(cart_payload())


@app.route("/checkout", methods=["POST"])
def checkout():
    delivery_key = request.form.get("delivery_service", "glovo")
    adapter = DELIVERY_ADAPTERS.get(delivery_key)

    if not adapter:
        return render_template(
            "checkout.html",
            status="error",
            messages=["Выбрана неизвестная служба доставки."],
            adapter_name="Неизвестный адаптер",
        )

    current_cart = cart_payload()
    if not current_cart["items"]:
        return render_template(
            "checkout.html",
            status="error",
            messages=["Корзина пуста. Добавьте блюда перед оформлением заказа."],
            adapter_name="Оформление заказа",
            order=None,
        )

    order = Order(
        customer_name=request.form.get("customer_name", "Гость FoodAdapter"),
        address=request.form.get("address", "Центр города, 24"),
        items=[
            OrderItem(name=item["name"], quantity=item["quantity"], price=item["price"])
            for item in current_cart["items"]
        ],
        total=current_cart["total"],
    )

    result = adapter.deliver_order(order)
    for message in result.messages:
        app.logger.info(message)

    session["cart"] = {}
    session.modified = True

    return render_template(
        "checkout.html",
        status="success",
        messages=result.messages,
        adapter_name=result.adapter_name,
        order=order,
    )


if __name__ == "__main__":
    app.run(debug=True)
