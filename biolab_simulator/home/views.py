from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest
from django.views import View
from . import models
from density.models import PredictiveModel as DensityModels


class Home(View):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        home = models.Home.objects.filter(id='1').first()
        density_models = DensityModels.objects.all
        # TODO: Add a query to get all the predictive models associated to each prop
        context = {'home': home,
        'density_models': density_models}

        return render(request, self.template_name, context)


def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)

def contact(request):
    template_name = 'home/contact.html'
    return render(request, template_name)