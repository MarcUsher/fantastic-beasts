from django.shortcuts import render
from django.http import HttpResponse
from .models import Beast
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Class-Based Views

class BeastList(ListView):
    model = Beast


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Replaced with CBV above
# def beasts_index(request):
#     beasts = Beast.objects.all()
#     return render(request, 'beasts/index.html', { 'beasts': beasts })

def beasts_detail(request, beast_id):
    beast = Beast.objects.get(id=beast_id)
    return render(request, 'beasts/detail.html', { 'beast': beast })