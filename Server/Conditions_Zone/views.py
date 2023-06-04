from django.shortcuts import render, redirect, Http404
from django.views.generic import CreateView, DeleteView, ListView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy

from django.http import HttpResponse

from .models import *
# from .utils import *

def terms_of_use(request):
    condition_bd = Conditions_Using.objects.all()
    return render(request, 'condition/terms_use.html', {'info': condition_bd})

def privacy_policy(request):
    condition_bd = Conditions_Confidentiality.objects.all()
    return render(request, 'condition/privacy_policy.html', {'info': condition_bd})