from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, "shop/index.html")

def register(request):
    return render(request, "shop/register.html")

def collections(request):
    category = Category.objects.filter(status = 0)
    return render(request, "shop/collections.html", {"category":category})

def collectionsview(request,name):
    if (Category.objects.filter(name=name,status = 0)):
        products = Product.objects.filter(category__name = name)
        return render(request, "shop/products/index.html", {"products":products})
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('')
 