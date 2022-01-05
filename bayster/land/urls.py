from django.urls import path

from . import views

urlpatterns = [
    path('land/', views.LandListView.as_view(), name='land-list'),
    path('detail/<int:pk>/', views.LandDetailView.as_view(), name='land-detail'),
    path('create/', views.LandCreateView.as_view(), name='land-create'),
]