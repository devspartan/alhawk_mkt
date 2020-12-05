from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.
def index(request):
    category_id = request.GET.get('category')

    if category_id:
        if category_id == 'all':
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)
