from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import User
from django.core.mail import send_mail

from django.contrib import messages
# Create your views here.

def signUp(request):
    form = CreateUserForm()

    if request.method == 'POST':
        email_msg = None
        phone_num_msg = None
        password_msg = None
        form_data = CreateUserForm(request.POST)
        print(form_data.is_valid())
        if form_data.is_valid():
            name = form_data.cleaned_data['full_name']
            email = form_data.cleaned_data['email']
            phone_num = form_data.cleaned_data['phone_num']
            password = form_data.cleaned_data['password']
            confirm_password = form_data.cleaned_data['confirm_password']

            if_user = User.objects.filter(email=email)
            if len(if_user):
                print("hey man im in registered")
                messages.error(request, "This email is already registered")
            else:
                messages.success(request, "Account Creates succesfully")
                return redirect('store:index')

            return render(request, 'signUp.html', {'form': form})
        else:
            print("im in out")
            return render(request, 'signUp.html', {'form': form})
    else:
        form = CreateUserForm()
        return render(request, 'signUp.html', {'form': form})


def login(request):

    return render(request, 'login.html')