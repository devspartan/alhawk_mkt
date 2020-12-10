from django.db import models
from accounts.models import User
from store.models import Product, Category

class Order(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.customer_id) + '  ' + str(self.customer)

    @property
    def get_ordered_products(self):
        # orderitems = OrderItem.objects.all() # for all the items
        orderitems = OrderItem.objects.filter(delivered=False)  # undelivered only

        my_products = []
        for item in orderitems:
            if item.product:
                for scq in item.product.size_color_quantity_set.all():
                    my_products.append([scq, item.date_added, item])

        return my_products

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    delivered = models.BooleanField(default=False, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.product) + '  ' + str(self.order) + '  ' + str(self.id)

    # @property
    # def get_price(self):
    #     price = self.product.price
    #     if self.product.offer:
    #         mrp = price
    #         offer = self.product.offer
    #         price = mrp - (mrp * offer // 100)
    #     return price

    # @property
    # def get_total(self):
    #     total = self.get_price * self.quantity
    #     return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class wishlist(models.Model):
    email = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100)


class CartItems(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer) + ' ' + str(self.product) + ' ' + str(self.quantity)

    @property
    def get_total_by_product(self):
        return self.product.price * self.quantity

    def get_total_by_cart(self, customer):
        products = self.objects.filter(customer=customer)
        total = 0
        for item in products:
            total = item.get_total_by_product + total

        return total