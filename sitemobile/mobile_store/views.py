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
            "status_class": "success",
            "status_text": "В наличии"
    }]
    data["products"] = products
    return render(request, "mobile_store/inventory.html", context=data)