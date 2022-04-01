from http.client import HTTPResponse
from multiprocessing import context
from urllib import request
from django.contrib import messages
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

    #TODO: Establish procedure to predict property from POST data and return the predicted value in the template
    def post(self, request, *args, **kwargs):
        self.model = self.model.objects.get(name=self.kwargs['name'])
        if request.method == 'POST':
            form = request.POST.dict()
            compounds = {}
            sum = 0
            for compound, value in form.items():
                if compound != 'csrfmiddlewaretoken' and value and int(value):
                    compounds[compound] = {'composition': int(value)}
                    sum += int(value)

                    parameters_set = self.model.compound_set.get(esther_type=compound.split(' ')[0], name=compound.split(' ')[1]).parameter_set.all()

                    for parameter in parameters_set:
                        compounds[compound][parameter.name] = parameter.value

            #TODO: Insert an action when the user sends an totally empty form
            context = {
                'form': form,
                'compounds': compounds,
            }

            if sum != 100:
                messages.warning(self.request,
                "The sum of compounds' mass percentage is not equal to 100%, this might affect the property prediction.")
                return render(request, 'density/helloworld.html', context)
            else:
                messages.success(self.request,
                "Property predicted successfully.")

            return render(request, 'density/helloworld.html', context)