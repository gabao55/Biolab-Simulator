from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View

# Create your views here.
def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)
