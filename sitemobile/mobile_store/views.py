from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Первая страница сайта на Django")

def catalog(request, category):
    print(request.GET)
    return HttpResponse(f"<h1>Каталог товаров<h1><p>Категория: {category}</p>")