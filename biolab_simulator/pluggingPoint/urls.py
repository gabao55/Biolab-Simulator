from django.urls import path
from . import views

app_name = 'pluggingPoint'

urlpatterns = [
    path('', views.PluggingPoint.as_view(), name='pluggingPoint'),
    path('Li-Bing-et-al./', views.LiBing.as_view(), name="li_bing"),
]
