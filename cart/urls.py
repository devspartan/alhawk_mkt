from django.urls import path
from .views import cartView

app_name = 'cart'

urlpatterns = [
    path('', cartView, name='cartView')
]

