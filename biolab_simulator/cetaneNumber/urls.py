from django.urls import path
from . import views

app_name = 'cetaneNumber'

urlpatterns = [
    path('', views.cetaneNumber, name='cetaneNumber'),
    path('<str:name>/', views.PredictiveModel.as_view(), name='cetane_number_model'),
]
