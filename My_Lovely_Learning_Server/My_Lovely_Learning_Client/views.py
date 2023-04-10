from django.shortcuts import render, redirect, Http404
from django.views.generic import CreateView, DeleteView, ListView
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'My_Lovely_Learning_templates/home.html')

def catalog(request):
    return render(request, 'My_Lovely_Learning_templates/catalog.html')

def redirect_to_main(request):
    return redirect('main', permanent=True)

class RegisterUser(CreateView):
    form_class = RegisterUserFormtemplate_name = 'My_Lovely_Learning_templates/register.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'My_Lovely_Learning_templates/login.html'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def get_success_url(self) -> str:
        return reverse_lazy('main')