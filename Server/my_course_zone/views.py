from django.shortcuts import render

# Create your views here.

def my_cource(request):
    return render(request, 'templates_myCource/user_learn_cource.html')
