from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import *

# Create your views here.

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('main')
    template_name = "settings/settings_password.html"

def main_settings(request):
    return render(request, 'settings/settings_user.html')

def email_settings(request):
    return render(request, 'settings/settings_email.html')