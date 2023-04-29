from django.shortcuts import render

# Create your views here.
def edit_main(request):
    return render(request, 'edit_template/edit_learn_template.html')