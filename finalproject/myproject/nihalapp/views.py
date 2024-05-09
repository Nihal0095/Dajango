from django.shortcuts import render,get_object_or_404

# Create your views here.
from . models import products
def home(request):
    mem=products.objects.all()
    return render (request,'home.html',{'mem':mem})

def shoes(request):
    mem=products.objects.all()
    return render (request,'shoes.html',{'mem':mem})

def mens(request):
    mem=products.objects.all()
    return render (request,'mens.html',{'mem':mem})

def detail_page(request,id):
    obj=get_object_or_404(products,pk=id)
    return render(request,'details.html',{'obj':obj})

