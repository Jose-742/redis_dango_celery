from django.urls import path, include
from apps.base.views import index

urlpatterns = [
    path('', index, name='index'),
]
