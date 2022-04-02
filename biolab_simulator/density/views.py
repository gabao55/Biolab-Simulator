from http.client import HTTPResponse
from multiprocessing import context
from unittest import result
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


#Template I was using before, but it's not needed
#TODO: Remove class PredictiveModel
class PredictiveModel(DetailView):
    model = models.PredictiveModel
    template_name = 'density/model.html'
    
    def get(self, request, *args, **kwargs):
        self.model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        print(self.kwargs['name'])

        self.context = {
            'model': self.model,
        }

        return render(request, self.template_name, self.context)

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

            context = {
                'compounds': compounds,
            }
            
            if not compounds:
                messages.error(self.request,
                "Please insert parameters to predict property")

                return self.get(request, self.template_name, name=self.kwargs['name'])

            elif sum != 100:
                messages.warning(self.request,
                "The sum of compounds' mass percentage is not equal to 100%, this might affect the property predicted.")
            else:
                messages.success(self.request,
                "Property predicted successfully.")

            return render(request, 'density/predicted_property.html', context)


class MurnaghanEquation(DetailView):
    template_name = 'density/model.html'
    model = get_object_or_404(models.PredictiveModel,
        name='Murnaghan Equation')
    context = {
        'model': model,
    }

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)

    #TODO: Establish procedure to predict property from POST data and return the predicted value in the template predicted_property.html
    #TODO: After structure is done, add new compounds and parameters and build some tests
    def post(self, request, *args, **kwargs):
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

            self.context['result'] = compounds
            
            if not compounds:
                messages.error(self.request,
                "Please insert parameters to predict property")

                return self.get(request, self.template_name)

            elif sum != 100:
                messages.warning(self.request,
                "The sum of compounds' mass percentage is not equal to 100%, this might affect the property predicted.")
            else:
                messages.success(self.request,
                "Property predicted successfully.")

            return render(request, self.template_name, self.context)