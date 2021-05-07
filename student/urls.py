from django.urls import path
from .views import Update_products
urlpatterns=[
    path('', Update_products, name="form"),
]