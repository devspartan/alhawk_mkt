from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

