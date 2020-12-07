from django.urls import path
from .views import signUpView, loginView, user_profile, logoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', signUpView, name='signup'),
    path('login/', loginView, name='login'),
    path('user/', user_profile, name='user_profile'),
    path('logout/', logoutView, name='logout')
]