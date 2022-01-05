from django.shortcuts import render
from django.views.generic import ListView

from .models import Land

# Create your views here.

class LandListView(ListView):
    model = Land
    template_name = 'land/land_list.html'