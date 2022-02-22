from django.urls import path
from .models import PredictiveModel
from . import views

app_name = 'density'

urlpatterns = [
    path('', views.density, name='density'),
    path('<str:name>/', views.PredictiveModel.as_view(), name='density_model'),
]