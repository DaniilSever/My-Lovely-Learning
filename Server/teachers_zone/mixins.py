from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q

def index(request):
    return render(request, "teaching/index.html")

class ListOwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(Q(owners__exact=self.request.user))