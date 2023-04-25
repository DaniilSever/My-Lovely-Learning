from django.shortcuts import render

# Create your views here.

def my_cource(request):
    return render(request, 'templates_myCource/user_learn_cource.html')

def favorit_cource(request):
    return render(request, 'templates_myCource/user_learn_cource_favorit.html')

def archiv_cource(request):
    return render(request, 'templates_myCource/user_learn_cource_archiv.html')

def class_cource(request):
    return render(request, 'templates_myCource/user_learn_class.html')