from django.urls import path
from . import views

app_name = 'cetaneNumber'

urlpatterns = [
    path('', views.cetaneNumber, name='cetaneNumber'),
]
