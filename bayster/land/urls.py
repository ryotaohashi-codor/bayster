from django.urls import path

from . import views

urlpatterns = [
    path('land/', views.LandListView.as_view(), name='land-list'),
    path('review/<int:land_id>/', views.LandReviewView.as_view(), name='land-review'),
    path('create/', views.LandCreateView.as_view(), name='land-create'),
]