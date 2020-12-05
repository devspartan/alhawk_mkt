from django.urls import path
from .views import signUp, login

app_name = 'accounts'

urlpatterns = [
    path('signup/', signUp, name='signup'),
    path('login/', login, name='login'),
]