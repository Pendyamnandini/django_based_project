from django.urls import path
from . import views

urlpatterns = [
    path('', views.heart, name='home'),
    path('heart/', views.heart, name='heart'),
    path('diabetes/', views.diabetes, name='diabetes'),
    path('breast/', views.breast, name='breast'),
]