from django.contrib import admin
from .models import Product, Category


class AdminProduct(admin.ModelAdmin):
     list_display = ['name', 'price', 'category']
# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)