from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("Первая страница сайта на Django")

def catalog(request, category):
    if request.GET:
        print(request.GET)
        url = reverse("catalog/", args=(request.GET[0]))
        return redirect("index")
    return HttpResponse(f'<h1>Каталог товаров</h1><p>Категория: {category}</p>')