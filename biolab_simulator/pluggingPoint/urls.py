from django.urls import path
from . import views

app_name = 'pluggingPoint'

urlpatterns = [
    path('', views.PluggingPoint.as_view(), name='pluggingPoint'),
    path('Su-Liu-Correlation/', views.SuLiu.as_view(), name="su_liu"),
    path('Sarin-et-al./', views.Sarin.as_view(), name="sarin"),
    path('Li-Bing-et-al./', views.LiBing.as_view(), name="li_bing"),
]
