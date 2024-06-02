from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from timeit import default_timer
# Create your views here.
def ShopIndex(request:HttpRequest)->HttpResponse:
    context = {
        "time": default_timer(),
    }
    return render(request,"shopapp/shop-index.html",context=context)