from django.shortcuts import render

# Create your views here.

def teachers_main(request):
    return render(request, 'teachers/teachers.html')