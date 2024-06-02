from .views import (
    ShopIndex,
    ProductsList,
    OrderList
)
from django.urls import path
app_name = 'shopapp'
urlpatterns = [
    path("", ShopIndex, name = "shop_index"),
    path("products/", ProductsList, name = "products_list"),
    path("orders/", OrderList, name = "orders_list"),
]