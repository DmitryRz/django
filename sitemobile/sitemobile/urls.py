from django.contrib import admin
from django.urls import path, include

from .views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobile_store/', include('mobile_store.urls')), 
]


handler404 = page_not_found