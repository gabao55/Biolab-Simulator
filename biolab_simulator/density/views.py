from http.client import HTTPResponse
from multiprocessing import context
from urllib import request
from django.http import HttpResponseRedirect
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
    template_name = 'density/model.html'
    
    def get(self, request, *args, **kwargs):
        self.form = ParametersForms
        self.model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        self.context = {
            'model': self.model,
        }

        return render(request, self.template_name, self.context)

    #TODO: Establish procedure to process data, predict property and return the predicted value in the template
    def post(self, request, *args, **kwargs):
        #TODO: Find a way to identify to which predictive model we are refering
        print(self.model.id)
        if request.method == 'POST':
            form = request.POST.dict()
            compounds = {}
            for compound, value in form.items():
                if compound != 'csrfmiddlewaretoken' and value:
                    compounds[compound] = value

            #TODO: Insert an action when the user sends an totally empty form
            context = {
                'form': form,
                'compounds': compounds,
            }

            return render(request, 'density/helloworld.html', context)