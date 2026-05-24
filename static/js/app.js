const toastElement = document.getElementById("app-toast");
const toastMessage = document.getElementById("toast-message");
const cartCount = document.getElementById("cart-count");

function showToast(message) {
    if (!toastElement || !toastMessage) return;
    toastMessage.textContent = message;
    bootstrap.Toast.getOrCreateInstance(toastElement).show();
}

async function postJson(url, payload) {
    const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });
    return response.json();
}

function updateCartBadge(cart) {
    if (cartCount) {
        cartCount.textContent = cart.count;
    }
}

document.querySelectorAll(".add-to-cart").forEach((button) => {
    button.addEventListener("click", async () => {
        button.classList.add("disabled");
        const cart = await postJson("/api/cart/add", { item_id: button.dataset.id });
        updateCartBadge(cart);
        showToast("Добавлено в корзину");
        button.classList.remove("disabled");
    });
});

function bindCartPage() {
    const cartList = document.getElementById("cart-list");
    const summaryCount = document.getElementById("summary-count");
    const summaryTotal = document.getElementById("summary-total");

    if (!cartList) return;

    async function refreshCart(cart) {
        updateCartBadge(cart);
        if (summaryCount) summaryCount.textContent = cart.count;
        if (summaryTotal) summaryTotal.textContent = `${cart.total} тг`;

        if (cart.items.length === 0) {
            window.location.reload();
        }
    }

    cartList.addEventListener("click", async (event) => {
        const quantityButton = event.target.closest(".quantity-btn");
        const removeButton = event.target.closest(".remove-btn");
        const row = event.target.closest(".cart-item");
        if (!row) return;

        if (quantityButton) {
            const input = row.querySelector("input");
            const nextQuantity = quantityButton.dataset.action === "plus"
                ? Number(input.value) + 1
                : Number(input.value) - 1;
            const cart = await postJson("/api/cart/update", {
                item_id: row.dataset.id,
                quantity: nextQuantity,
            });
            refreshCart(cart);
            window.location.reload();
        }

        if (removeButton) {
            const cart = await postJson("/api/cart/remove", { item_id: row.dataset.id });
            refreshCart(cart);
            window.location.reload();
        }
    });
}

bindCartPage();

document.querySelectorAll(".checkout-button").forEach((button) => {
    button.closest("form").addEventListener("submit", () => {
        button.querySelector(".button-text").textContent = "Адаптируем заказ...";
        button.querySelector(".spinner-border").classList.remove("d-none");
        button.disabled = true;
    });
});
