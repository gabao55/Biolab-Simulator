from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest
from django.views import View
from . import models


class Home(View):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        home = models.Home.objects.filter(id='1').first()
        context = {'home': home}

        return render(request, self.template_name, context)


    # def get_context_data(self, **kwargs):
    #     #TODO: Finish this query to get the data from DB
    #     self.model = get_object_or_404(models.Home, id=1)
    #     return self.model


def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)

def contact(request):
    template_name = 'home/contact.html'
    return render(request, template_name)