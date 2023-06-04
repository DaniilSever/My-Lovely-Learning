
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input height-40", "type": "password"}), label="Старый пароль")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input height-40", "type": "password"}), label="Новый пароль")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input height-40", "type": "password"}), label="Повтор пароля")
    
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")