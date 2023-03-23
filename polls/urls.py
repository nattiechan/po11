from django.urls import path
from .views import index

urlpatterns: list = [
    path('', index, name='index')
]