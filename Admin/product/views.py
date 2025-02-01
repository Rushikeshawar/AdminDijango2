from django.shortcuts import render
from .models import Product
def home(request):
    info = Product.objects.all()
    return render(request,"index.html" ,{"info":info})