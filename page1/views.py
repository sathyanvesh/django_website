from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Prodcuts


# Create your views here.

def CreateView(request):
    Products = Prodcuts.objects.all()
    context = {
        'Products' : Products
    }
    return render(request,'home.html',context)


def DetailView(request,pk):
    Product = Prodcuts.objects.get(id=pk)
    context = {
        'Product' : Product
    }
    return render(request,'detail.html',context)
