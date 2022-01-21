from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View

# Create your views here.
def density(request):
    template_name = 'density/density.html'
    return render(request, template_name)
