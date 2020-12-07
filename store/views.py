from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from accounts.models import User
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

    print(request.user, " :User")

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['user'] = request.user
    return render(request, 'index.html', data)
