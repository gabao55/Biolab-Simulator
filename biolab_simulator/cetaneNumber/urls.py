from django.urls import path
from . import views

app_name = 'cetaneNumber'

urlpatterns = [
    path('', views.CetaneNumber.as_view(), name='cetaneNumber'),
    path('Lapuerta-Rodriguez-Mora/', views.LapuertaRodriguez.as_view(), name='lapuerta_rodriguez'),
    path('Lapuerta-Rodriguez-Mora-only-FAME/', views.LapuertaRodriguezSimplified.as_view(), name='lapuerta_rodriguez_simplified'),
    path('<str:name>/', views.PredictiveModel.as_view(), name='cetaneNumber_model'),
]
