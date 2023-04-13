from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input-popup', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input-popup', 'placeholder': 'Электронная почта'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input-popup', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input-popup', 'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input-popup', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input-popup', 'placeholder': 'Пароль'}))
