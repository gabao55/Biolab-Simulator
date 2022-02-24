from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest
from django.views import View
from . import models


class Home(View):
    template_name = 'home/home.html'
    model = models.Home
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        #TODO: Finish this query to get the data from DB
        self.model = get_object_or_404(models.Home)
        return self.model


def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)

def contact(request):
    template_name = 'home/contact.html'
    return render(request, template_name)