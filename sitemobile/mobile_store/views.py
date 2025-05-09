from itertools import product
from django.shortcuts import render

data = { "company": "ООО Илья молодец"}

def index(request):
    data["active_page"] = "index"            
    return render(request, "mobile_store/index.html", context=data)


def dashboard(request):
    data["active_page"] = "dashboard"
    return render(request, "mobile_store/dashboard.html", context=data)


def inventory(request):
    data["active_page"] = "inventory"
    return render(request, "mobile_store/inventory.html", context=data)