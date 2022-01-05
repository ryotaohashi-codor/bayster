from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Land

# Create your views here.

class LandListView(ListView):
    model = Land
    template_name = 'land/land_list.html'

class LandDetailView(DetailView):
    model = Land
    template_name = 'land/land_detail.html'