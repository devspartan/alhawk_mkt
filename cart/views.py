from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View

from .models import *


# Create your views here.


def get_user_cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cartQuerySet = CartItems.objects.filter(customer=customer)

        data = {}
        total = 0
        for item in cartQuerySet:
            total = total + item.get_total_by_product
        data['cart'] = cartQuerySet
        data['total'] = total
        return data

    return "user not authenticated"


@login_required(login_url='accounts:login', redirect_field_name='cart:cartView')
def cartView(request):
    data = get_user_cart(request)

    if request.method == 'GET':

        return render(request, 'cart.html', data)

    elif request.method == 'POST':
        try:
            product_id = request.POST['increase']
            cart_obj = CartItems.objects.get(customer=request.user, product_id=product_id)
            cart_obj.quantity += 1
            cart_obj.save()
        except:
            pass
        try:
            product_id = request.POST['decrease']
            cart_obj = CartItems.objects.get(customer=request.user, product_id=product_id)
            cart_obj.quantity -= 1
            cart_obj.save()
            if cart_obj.quantity == 0:
                CartItems.objects.filter(quantity=0).delete()
        except:
            pass
        try:
            print("inm in delete")
            product_id = request.POST['delete']
            cart_obj = CartItems.objects.filter(customer=request.user, product_id=product_id).delete()

            print(cart_obj)
            # data['cart'] = cart_obj
        except:
            pass
        data = get_user_cart(request)

        return HttpResponseRedirect(reverse('cartView', args=(data,)))
        # return render(request, 'cart.html', data)
