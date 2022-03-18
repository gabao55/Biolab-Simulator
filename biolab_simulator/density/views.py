from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View
from . import models
from .forms import ParametersForms


class Density(View):
    template_name = 'density/density.html'

    def get(self, request, *args, **kwargs):
        density_models = models.PredictiveModel.objects.all
        context = {'density_models': density_models,}

        return render(request, self.template_name, context)


class PredictiveModel(DetailView):
    model = models.PredictiveModel

    def get(self, request, *args, **kwargs):
        form = ParametersForms
        model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        template_name = 'density/model.html'
        context = {
            'form': form,
            'model': model
        }

        return render(request, template_name, context)

    #TODO: Define POST method for processing data
    def post(self, request, *args, **kwargs):
        pass