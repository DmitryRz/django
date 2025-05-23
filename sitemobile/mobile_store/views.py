from itertools import product
from django.shortcuts import render
from mobile_store.models import Product


def get_base_context():
    return {
        "company": "ООО \"Мобильная связь\"",
    }


def index(request):
    context = get_base_context()
    context["active_page"] = "index"
    return render(request, "mobile_store/index.html", context)


def dashboard(request):
    context = get_base_context()
    context["active_page"] = "dashboard"
    return render(request, "mobile_store/dashboard.html", context)


def inventory(request, category_id=0):
    context = get_base_context()
    context["active_page"] = "inventory"
    context["current_category"] = category_id
    
    return render(request, "mobile_store/inventory.html", context)