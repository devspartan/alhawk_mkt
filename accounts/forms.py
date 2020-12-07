from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateUserForm(forms.Form):
    fields = ['full_name', 'email', 'phone_num', 'password']
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'required': 'required'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'required': 'required'}))
    phone_num = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone Num', 'class': 'form-control', 'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Create Password', 'class': 'form-control', 'required': 'required'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'required': 'required'}))


class LoginUserForm(forms.Form):
    fields = ['email', 'password']
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control', 'required': 'required'}))
