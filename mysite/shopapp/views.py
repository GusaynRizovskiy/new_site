from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from timeit import default_timer
from shopapp.models import Product,Order
# Create your views here.
def ShopIndex(request:HttpRequest)->HttpResponse:
    context = {
        "time": default_timer(),
    }
    return render(request,"shopapp/shop-index.html",context=context)
def ProductsList(request:HttpRequest)->HttpResponse:
    context = {
        "products": Product.objects.all()
    }
    return render(request,"shopapp/products-list.html",context=context)
def OrderList(request:HttpRequest)->HttpResponse:
    context = {
        "orders": Order.objects.all()
    }
    return render(request,"shopapp/orders-list.html",context=context)