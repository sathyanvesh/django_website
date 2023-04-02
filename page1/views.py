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


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        image = request.FILES["upload"]
        prod = Prodcuts(name=name,price=price,description=desc,image=image)
        prod.save()
    
    return render(request,'addprod.html')