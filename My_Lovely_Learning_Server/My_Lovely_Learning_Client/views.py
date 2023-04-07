from django.shortcuts import render, redirect, Http404

from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        return render(request, 'My_Lovely_Learning_templates/home.html', {"otvet": "yes"})

    return render(request, 'My_Lovely_Learning_templates/home.html')

def catalog(request):
    return render(request, 'My_Lovely_Learning_templates/catalog.html')

def redirectMe(request):
    return redirect('main')