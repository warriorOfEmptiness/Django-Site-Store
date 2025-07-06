from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'store/index.html')

def catalog(request):

    context = {

    }
    return render(request,'store/catalog.html',context)
