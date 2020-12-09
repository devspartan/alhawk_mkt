from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

from .models import *


# Create your views here.
class CartView(View):

    def get_user_cart(self, request):
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
    def get(self, request):
        data = self.get_user_cart(request)

        return render(request, 'cart.html', data)

    # @login_required(login_url='accounts:login', redirect_field_name='cart:cartView')
    def post(self, request):

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
        except:
            pass
        data = self.get_user_cart(request)
        return render(request, 'cart.html', data)
