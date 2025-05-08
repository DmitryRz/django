from itertools import product
from django.shortcuts import render

data = { "company": "ООО Мобильная связь"}

def index(request):
    return render(request, "mobile_store/index.html", context=data)


def dashboard(request):
    return render(request, "mobile_store/dashboard.html", context=data)


def inventory(request):
    products = [{
            "id": 1, 
            "name": "iPhone 14",
            "category": "Телефоны",
            "quantity": 10,
            "price": 100000,
            "status_text": "В наличии"
    }, {
            "id": 2,
            "name": "iPhone 13",
            "category": "Телефоны",
            "quantity": 0,
            "price": 80000,
            "status_text": "Нет в наличии"
    }, {
            "id": 3,
            "name": "iPhone 12",
            "category": "Телефоны",
            "quantity": 5,
            "price": 60000,
            "status_text": "В наличии"
    }]
    data["products"] = products
    return render(request, "mobile_store/inventory.html", context=data)