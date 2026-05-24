def get_categories():
    return [
        {"name": "Пицца", "icon": "fa-pizza-slice"},
        {"name": "Бургеры", "icon": "fa-burger"},
        {"name": "Суши", "icon": "fa-fish"},
        {"name": "Напитки", "icon": "fa-mug-hot"},
        {"name": "Десерты", "icon": "fa-ice-cream"},
    ]


def get_featured_restaurants():
    return [
        {"name": "Urban Slice", "rating": "4.9", "time": "20-30 мин", "tag": "Итальянская кухня"},
        {"name": "Nord Bowl", "rating": "4.8", "time": "25-35 мин", "tag": "Азиатская кухня"},
        {"name": "Burger Lab", "rating": "4.7", "time": "15-25 мин", "tag": "Стритфуд"},
    ]


def get_menu_items():
    return [
        {
            "id": "pizza-margherita",
            "name": "Маргарита Клауд",
            "description": "Моцарелла, томатный соус, базилик и оливковое масло.",
            "price": 3290,
            "category": "Пицца",
            "image": "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": "burger-smash",
            "name": "Смэш Бургер",
            "description": "Говяжья котлета, чеддер, маринованные огурцы и фирменный соус.",
            "price": 2790,
            "category": "Бургеры",
            "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": "sushi-set",
            "name": "Суши-сет Токио",
            "description": "Роллы с лососем, нигири с тунцом, васаби и имбирь.",
            "price": 4590,
            "category": "Суши",
            "image": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": "berry-lemonade",
            "name": "Ягодный лимонад",
            "description": "Газированный лимонад с ягодами и свежей мятой.",
            "price": 1290,
            "category": "Напитки",
            "image": "https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": "choco-dessert",
            "name": "Шоколадный велюр",
            "description": "Теплый брауни, ванильный крем и шоколадная глазурь.",
            "price": 1890,
            "category": "Десерты",
            "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": "pepperoni",
            "name": "Пепперони Сигнал",
            "description": "Острая пепперони, моцарелла и орегано.",
            "price": 3590,
            "category": "Пицца",
            "image": "https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=900&q=80",
        },
    ]
