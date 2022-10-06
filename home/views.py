from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest
from django.views import View
from . import models
from density.models import PredictiveModel as DensityModels
from cetaneNumber.models import PredictiveModel as CetaneNumberModels
from pluggingPoint.models import PredictiveModel as PluggingPointModels


class Home(View):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        home = models.Home.objects.filter(id='1').first()
        density_models = DensityModels.objects.all
        cetane_number_models = CetaneNumberModels.objects.all
        plugging_point_models = PluggingPointModels.objects.all
        context = {'home': home,
        'density_models': density_models,
        'cetane_number_models': cetane_number_models,
        'plugging_point_models': plugging_point_models,}

        return render(request, self.template_name, context)


def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)

def contact(request):
    template_name = 'home/contact.html'
    return render(request, template_name)