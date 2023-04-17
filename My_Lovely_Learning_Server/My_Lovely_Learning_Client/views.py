from django.shortcuts import render, redirect, Http404
from django.views.generic import CreateView, DeleteView, ListView
from django.contrib.auth.views import LoginView 
from django.contrib.auth import logout, login
from django.urls import reverse_lazy

from django.http import HttpResponse

from .forms import *
from .models import *
# from .utils import *

# Create your views here.

def index(request):
    if request.method == 'post':
       pass

    return render(request, 'My_Lovely_Learning_templates/home.html')

class RegisterUser(CreateView):
    form_class = regUserForm
    template_name = 'My_Lovely_Learning_templates/reg.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main') 

class LoginUser(LoginView):
    form_class = loginUserForm
    template_name = 'My_Lovely_Learning_templates/home.html'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_success_url(self) -> str:
        return reverse_lazy('main')

def logout_user(request):
    logout(request)
    return redirect('main')

def redirectMe(request):
    return redirect('main')