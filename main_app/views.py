from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Beast, Location
from .forms import WalkForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Home & About views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')




# Beast Views

class BeastList(ListView):
    model = Beast

# Replaced with CBV above
# def beasts_index(request):
#     beasts = Beast.objects.all()
#     return render(request, 'beasts/index.html', { 'beasts': beasts })

def beasts_detail(request, beast_id):
    beast = Beast.objects.get(id=beast_id)
    walk_form = WalkForm()
    unused_locations = Location.objects.exclude(id__in = beast.locations.all().values_list('id'))
    return render(request, 'beasts/detail.html', { 'beast': beast, 'walk_form': walk_form, 'locations': unused_locations })


class BeastCreate(CreateView):
    model = Beast
    fields = '__all__'

class BeastUpdate(UpdateView):
    model = Beast
    fields = ['native', 'description', 'size', 'danger']

class BeastDelete(DeleteView):
    model = Beast
    success_url = '/beasts/'



# Walk views

def add_walk(request, beast_id):
    form = WalkForm(request.POST)
    if form.is_valid():
        new_walk = form.save(commit=False)
        new_walk.beast_id = beast_id
        new_walk.save()
        return redirect('beast_detail', beast_id = beast_id)



# Location Views

class LocationList(ListView):
    model = Location

class LocationDetail(DetailView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

class LocationUpdate(UpdateView):
    model = Location
    fields = '__all__'

class LocationDelete(DeleteView):
    model = Location
    success_url = '/locations/'


# Association Views

def assoc_location(request, beast_id, location_id):
    Beast.objects.get(id=beast_id).locations.add(location_id)
    return redirect('beast_detail', beast_id=beast_id)

def disassoc_location(request, beast_id, location_id):
    Beast.objects.get(id=beast_id).locations.remove(location_id)
    return redirect('beast_detail', beast_id=beast_id)