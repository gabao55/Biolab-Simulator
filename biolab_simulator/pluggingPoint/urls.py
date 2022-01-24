from django.urls import path
from . import views

app_name = 'pluggingPoint'

urlpatterns = [
    path('', views.pluggingPoint, name='pluggingPoint')
]
