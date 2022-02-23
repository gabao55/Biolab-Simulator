from django.urls import path
from . import views

app_name = 'pluggingPoint'

urlpatterns = [
    path('', views.pluggingPoint, name='pluggingPoint'),
    path('<str:name>/', views.PredictiveModel.as_view(), name='pluggingPoint_model'),
]
