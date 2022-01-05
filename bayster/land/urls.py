from django.urls import path

from . import views

urlpatterns = [
    path('land/', views.LandListView.as_view(), name='land-list'),
]