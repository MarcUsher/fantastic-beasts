from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Beast
from .forms import WalkForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Class-Based Views

class BeastList(ListView):
    model = Beast


class BeastCreate(CreateView):
    model = Beast
    fields = '__all__'

class BeastUpdate(UpdateView):
    model = Beast
    fields = ['native', 'description', 'size', 'danger']

class BeastDelete(DeleteView):
    model = Beast
    success_url = '/beasts/'

# Create your views here

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
    walk_form = WalkForm()
    return render(request, 'beasts/detail.html', { 'beast': beast, 'walk_form': walk_form })


def add_walk(request, beast_id):
    form = WalkForm(request.POST)
    if form.is_valid():
        new_walk = form.save(commit=False)
        new_walk.beast_id = beast_id
        new_walk.save()
        return redirect('detail', beast_id = beast_id)