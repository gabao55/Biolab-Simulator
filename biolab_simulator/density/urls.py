from django.urls import path
from .models import PredictiveModel
from . import views

app_name = 'density'

urlpatterns = [
    path('', views.Density.as_view(), name='density'),
    path('Murnaghan-Equation/', views.MurnaghanEquation.as_view(), name='murnaghan_equation')
]