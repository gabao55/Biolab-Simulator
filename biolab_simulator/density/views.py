from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def density(request):
    return render(request, 'density/home.html')