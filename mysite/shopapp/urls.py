from .views import ShopIndex
from django.urls import path
app_name = 'shopapp'
urlpatterns = [
    path("", ShopIndex, name = "shop_index"),
]