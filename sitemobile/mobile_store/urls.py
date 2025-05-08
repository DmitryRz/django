from django.urls import path, register_converter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
]