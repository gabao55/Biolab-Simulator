from django.urls import path
from . import views

app_name = 'cetaneNumber'

urlpatterns = [
    path('', views.CetaneNumber.as_view(), name='cetaneNumber'),
    path('<str:name>/', views.PredictiveModel.as_view(), name='cetaneNumber_model'),
]
