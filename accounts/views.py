from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import User


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
                if password != confirm_password:
                    messages.error(request, "Password doesn't match")
                else:
                    messages.success(request, "Account Created succesfully")
                    return redirect('store:index')

        else:
            messages.error(request, "Enter valid phone number")

        return render(request, 'signUp.html', {'form': form_data})

    else:
        form_data = CreateUserForm()
    return render(request, 'signUp.html', {'form': form_data})


def login(request):
    return render(request, 'login.html')
