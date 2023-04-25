from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

from .models import *

class regUserForm(UserCreationForm):
    username = forms.CharField(label='Введите логин:', widget=forms.TextInput(attrs={'class': 'reg-input', 'placeholder': 'Логин...'}))
    email = forms.EmailField(label='Введите Email:', widget=forms.EmailInput(attrs={'class': 'reg-input', 'placeholder': 'Почта...'}))
    password1 = forms.CharField(label='Введите пароль:', widget=forms.PasswordInput(attrs={'class': 'reg-input', 'placeholder': 'Пароль...'}))
    password2 = forms.CharField(label='Подтвердите пароль:', widget=forms.PasswordInput(attrs={'class': 'reg-input', 'placeholder': 'Повтор пароля...'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class loginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input-popup', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input-popup', 'placeholder': 'Пароль'}))

class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input height-40", "type": "password"}), label="Старый пароль")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input height-40", "type": "password"}), label="Новый пароль")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input height-40", "type": "password"}), label="Повтор пароля")
    
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")