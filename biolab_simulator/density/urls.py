from django.urls import path

from biolab_simulator.density.models import PredictiveModel
from . import views

app_name = 'density'

urlpatterns = [
    path('', views.density, name='density'),
    path('/<str:name>', views.PredictiveModel.as_view()),
]