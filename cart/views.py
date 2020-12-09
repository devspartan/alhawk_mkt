from django.shortcuts import render
from .models import *

# Create your views here.
def cartView(request):
    if request.user.is_authenticated:
        customer = request.user
        cartQuerySet = CartItems.objects.filter(customer=customer)
        data = {}
        total = 0
        for item in cartQuerySet:
            total = total + item.get_total_by_product
        data['cart'] = cartQuerySet
        data['total'] = total
    return render(request, 'cart.html', data)