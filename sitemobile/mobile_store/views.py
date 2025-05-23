from itertools import product
from django.shortcuts import render

data = { "company": "ООО \"Мобильная связь\""}

FILTER_BAR = [
        {'id': 0, 'name': 'Все категории'},
        {'id': 1, 'name': 'Смартфоны'},
        {'id': 2, 'name': 'Планшеты'},
        {'id': 3, 'name': 'Аксессуары'},
        {'id': 4, 'name': 'SIM-карты'}
        ]

ALL_PRODUCTS = [
    {'id': 1, 'name': 'iPhone 13', 'category': 'Смартфоны', 'quantity': 10, 'price': 60000, 'status': 'active'},
    {'id': 2, 'name': 'Samsung Galaxy S21', 'category': 'Смартфоны', 'quantity': 5, 'price': 50000, 'status': 'active'},
    {'id': 3, 'name': 'iPad Pro', 'category': 'Планшеты', 'quantity': 8, 'price': 80000, 'status': 'active'},
    {'id': 4, 'name': 'Чехол для iPhone', 'category': 'Аксессуары', 'quantity': 20, 'price': 2000, 'status': 'active'},
    {'id': 5, 'name': 'SIM-карта МТС', 'category': 'SIM-карты', 'quantity': 50, 'price': 500, 'status': 'active'},
    {'id': 6, 'name': 'Xiaomi Redmi Note 10', 'category': 'Смартфоны', 'quantity': 7, 'price': 25000, 'status': 'active'},
    {'id': 7, 'name': 'Samsung Galaxy Tab S7', 'category': 'Планшеты', 'quantity': 4, 'price': 45000, 'status': 'active'},
    {'id': 8, 'name': 'Huawei MatePad', 'category': 'Планшеты', 'quantity': 3, 'price': 30000, 'status': 'active'},
    {'id': 9, 'name': 'Наушники AirPods', 'category': 'Аксессуары', 'quantity': 15, 'price': 15000, 'status': 'active'},
    {'id': 10, 'name': 'Карта памяти 128GB', 'category': 'Аксессуары', 'quantity': 12, 'price': 3000, 'status': 'active'},
    {'id': 11, 'name': 'SIM-карта Мегафон', 'category': 'SIM-карты', 'quantity': 40, 'price': 500, 'status': 'active'},
    {'id': 12, 'name': 'SIM-карта Билайн', 'category': 'SIM-карты', 'quantity': 35, 'price': 500, 'status': 'active'}
]

def index(request):
    data["active_page"] = "index"            
    return render(request, "mobile_store/index.html", context=data)


def dashboard(request):
    data["active_page"] = "dashboard"
    return render(request, "mobile_store/dashboard.html", context=data)


def inventory(request, category_id=0):
    data = {
        "active_page": "inventory",
        "current_category": category_id,
        "filter_bar": FILTER_BAR
    }

    if category_id == 0:
        data["products"] = ALL_PRODUCTS
    else:
        category_name = next(
            (item['name'] for item in FILTER_BAR if item['id'] == category_id),
            None
        )

        data["products"] = [
            product for product in ALL_PRODUCTS
            if product['category'] == category_name
        ]

    return render(request, "mobile_store/inventory.html", context=data)