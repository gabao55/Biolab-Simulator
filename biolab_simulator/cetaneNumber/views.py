from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from . import models


class CetaneNumber(View):
    template_name = 'cetaneNumber/cetaneNumber.html'

    def get(self, request, *args, **kwargs):
        predictive_models = models.PredictiveModel.objects.all
        context = {'predictive_models': predictive_models,}

        return render(request, self.template_name, context)
        

class PredictiveModel(DetailView):
    model = models.PredictiveModel
    template_name = 'cetaneNumber/lapuerta_rodriguez.html'
    context_object_name = 'model'

    def get_object(self):
        self.model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        return self.model


class LapuertaRodriguez(DetailView):
    template_name = "cetaneNumber/lapuerta_rodriguez.html"
    model = get_object_or_404(models.PredictiveModel,
        name = "La Puerta, Rodríguez and Mora")

    context = {
        "model": model,
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)