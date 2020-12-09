from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
from cart.models import CartItems
from accounts.models import User
from django.views import View
# Create your views here.

class Index(View):

    def get(self, request):
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


    def post(self, request):
        print(request.user, request.POST['product'])
        user = User.objects.get(email=request.user)
        product = Product.objects.get(id=request.POST['product'])
        obj = None
        try:
            obj = CartItems.objects.get(product=product, customer=user)
        except:
            pass
        print(user, product, 'post_request')
        print(obj, "hey mann")
        if obj:
            obj.quantity = obj.quantity+1
            obj.save()
        else:
            CartItems.objects.create(customer=user, product=product, quantity=1)
        return redirect('store:index')

