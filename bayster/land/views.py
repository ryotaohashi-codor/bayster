from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import LandReviewForm, LandForm
from .models import Land, LandReview

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Create your views here.

class LandListView(ListView):
    model = Land
    template_name = 'land/land_list.html'
    ordering = ['-applied_date']

class LandReviewView(LoginRequiredMixin, CreateView):
    form_class = LandReviewForm
    model = LandReview
    template_name = 'land/land_review.html'
    success_url = reverse_lazy('land-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = Land.objects.get(pk=self.kwargs['land_id'])
        return context

class LandCreateView(LoginRequiredMixin, CreateView):
    model = Land
    template_name = 'land/land_create.html'
    form_class = LandForm
    success_url = reverse_lazy('land-list')

    def form_valid(self, form):
        messages.success(self.request, '申請が完了しました')
        form.instance.user = self.request.user
        return super().form_valid(form)
