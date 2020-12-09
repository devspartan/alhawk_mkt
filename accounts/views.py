from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
from .forms import CreateUserForm, LoginUserForm
from .models import User


def signUpView(request):
    if request.method == 'POST':
        form_data = CreateUserForm(request.POST)
        if form_data.is_valid():
            name = form_data.cleaned_data['full_name']
            email = form_data.cleaned_data['email']
            phone_num = form_data.cleaned_data['phone_num']
            password = form_data.cleaned_data['password']
            confirm_password = form_data.cleaned_data['confirm_password']

            if User.objects.filter(email=email):
                messages.error(request, "This email is already registered")
            else:
                if password != confirm_password:
                    messages.error(request, "Password doesn't match")
                else:
                    messages.success(request, "Account Created succesfully")
                    User.objects.create(name=name, email=email, phone_num=phone_num, password=make_password(password))
                    return redirect('store:index')
        else:
            messages.error(request, "Enter valid phone number")
        return render(request, 'signUp.html', {'form': form_data})
    else:
        form_data = CreateUserForm()
    return render(request, 'signUp.html', {'form': form_data})


def loginView(request):
    print(request.user, "user")
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email=email)
            if user is not None:
                user = authenticate(username=email, password=password)
                if user is not None:
                    print('im in user ')
                    login(request, user)
                    request.session['user_id'] = user.id
                    request.session['user_email'] = user.email
                    return redirect('store:index')
                else:
                    messages.error(request, "Password doesn't match")
            else:
                messages.error(request, "Email not registered")

            return render(request, 'login.html', {'form': form})
    form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('store:index')

def user_profile(request):
    user_obj = request.user
    return render(request, 'user_profile.html', {'user_obj': user_obj})
