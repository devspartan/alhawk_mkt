from django.urls import path
from .views import index, signUp, login

urlpatterns = [
    path('', index),
    path('signup/', signUp),
    path('login/', login)
]
