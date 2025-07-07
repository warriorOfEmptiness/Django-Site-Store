from django.shortcuts import render
from . models import Product, ProductCategory

# Create your views here.

def index(request):
    return render(request,'store/index.html')

def catalog(request):
    product = Product.objects.all()
    context = {
        'product':product,
    }
    return render(request,'store/catalog.html',context)
