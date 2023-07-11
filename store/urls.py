from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
]
