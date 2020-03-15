from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request) :
    products = Product.objects.all()
    return(render(request, 'inventory/home.html', {'products':products}))

def about(request) :
    return(render(request, 'inventory/about.html'))

def add_product(request) :
    if request.method == 'POST' :
        form = ProductForm(request.POST)
        if form.is_valid() :
            form.save()
            return(redirect('/'))
    return(render(request, 'inventory/add_product.html'))

def update_product(request, pk) :
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST' :
        form = ProductForm(request.POST, instance=product)
        if form.is_valid() :
            form.save()
            return(redirect('/'))
    return(render(request, 'inventory/update_product.html',{'form':form}))

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST' :
        product.delete()
        return(redirect('/'))
    return(render(request, 'inventory/delete_product.html', {'product':product}))