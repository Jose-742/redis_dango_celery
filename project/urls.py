
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('', include('admin_soft.urls')),
    
]
