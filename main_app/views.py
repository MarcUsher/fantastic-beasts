from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Beast, Location
from .forms import WalkForm, NewUserForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


# Home & About views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')




# Beast Views

class BeastList(LoginRequiredMixin, ListView):
    # model = Beast
    # context_object_name = 'beast'
    # queryset = Beast.objects.filter(user=request.user)
    def get_queryset(self):
        my_beasts = Beast.objects.filter(user=self.request.user)
        return my_beasts


# Replaced with CBV above
# def beasts_index(request):
#     beasts = Beast.objects.all()
#     return render(request, 'beasts/index.html', { 'beasts': beasts })


@login_required
def beasts_detail(request, beast_id):
    beast = Beast.objects.get(id=beast_id)
    walk_form = WalkForm()
    unused_locations = Location.objects.exclude(id__in = beast.locations.all().values_list('id'))
    return render(request, 'beasts/detail.html', { 'beast': beast, 'walk_form': walk_form, 'locations': unused_locations })


class BeastCreate(LoginRequiredMixin, CreateView):
    model = Beast
    fields = ['name', 'native', 'description', 'size', 'danger', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BeastUpdate(LoginRequiredMixin, UpdateView):
    model = Beast
    fields = ['native', 'description', 'size', 'danger']

class BeastDelete(LoginRequiredMixin, DeleteView):
    model = Beast
    success_url = '/beasts/'



# Walk views

@login_required
def add_walk(request, beast_id):
    form = WalkForm(request.POST)
    if form.is_valid():
        new_walk = form.save(commit=False)
        new_walk.beast_id = beast_id
        new_walk.save()
        return redirect('beast_detail', beast_id = beast_id)



# Location Views

class LocationList(LoginRequiredMixin, ListView):
    model = Location

class LocationDetail(LoginRequiredMixin, DetailView):
    model = Location

class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    fields = '__all__'

class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    fields = '__all__'

class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = '/locations/'


# Association Views

@login_required
def assoc_location(request, beast_id, location_id):
    Beast.objects.get(id=beast_id).locations.add(location_id)
    return redirect('beast_detail', beast_id=beast_id)

@login_required
def disassoc_location(request, beast_id, location_id):
    Beast.objects.get(id=beast_id).locations.remove(location_id)
    return redirect('beast_detail', beast_id=beast_id)



# SIGNUP View

# def signup(request):
#     error_message = ''

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('beast_index')
#         else:
#             error_message = "Invalid sign up - try again!"
    
#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)




def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('beast_index')
        else:
            error_message = "Invalid sign up - try again!"
    
    form = NewUserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class PasswordResetByUser(PasswordChangeView):
  template_name = 'registration/password_change_form.html'
  success_url = '/'
