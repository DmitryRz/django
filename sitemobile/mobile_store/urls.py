from django.urls import path, register_converter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/<str:category>/', views.catalog, name='catalog'),
]