from django.urls import path
from . import views

app_name = 'density'

urlpatterns = [
    path('', views.density, name='density')
]