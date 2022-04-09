from http.client import HTTPResponse
from multiprocessing import context
from unittest import result
from urllib import request
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View
from . import models
from .utils import murnaghan_equation_predict


class Density(View):
    template_name = 'density/density.html'

    def get(self, request, *args, **kwargs):
        density_models = models.PredictiveModel.objects.all
        context = {'density_models': density_models,}

        return render(request, self.template_name, context)


class MurnaghanEquation(DetailView):
    template_name = 'density/murnaghan_equation.html'
    model = get_object_or_404(models.PredictiveModel,
        name='Murnaghan Equation')

    intensive_parameters = ['Temperature (K)', "Pressure (MPa)", "Atmospheric density (kg/m³)"]
    context = {
        'model': model,
        'intensive_parameters': intensive_parameters,
    }

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.context)

    #TODO: Build some tests
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()
            
            intensive_parameters = {"Temperature": int(form["Temperature (K)"]) if form['Temperature (K)'] else '',
            "Pressure": int(form["Pressure (MPa)"]) if form["Pressure (MPa)"] else '',
            "Atmospheric density": int(form["Atmospheric density (kg/m³)"]) if form["Atmospheric density (kg/m³)"] else '',
            }

            form.pop("Temperature (K)")
            form.pop("Pressure (MPa)")
            form.pop("Atmospheric density (kg/m³)")

            compounds = {}
            sum = 0
            for compound, value in form.items():
                if compound != 'csrfmiddlewaretoken' and value and int(value):
                    compounds[compound] = {'composition': int(value)}
                    sum += int(value)

                    parameters_set = self.model.compound_set.get(esther_type=compound.split(' ')[0], name=compound.split(' ')[1]).parameter_set.all()

                    for parameter in parameters_set:
                        compounds[compound][parameter.name] = parameter.value

            if not intensive_parameters['Temperature'] \
            or not intensive_parameters['Pressure'] \
            or not intensive_parameters['Atmospheric density']:
                messages.error(self.request,
                "Please insert all intensive parameters to predict property")

                return self.get(request, self.template_name)
            
            elif not compounds:
                messages.error(self.request,
                "Please insert compounds' mass percentage to predict property")

                return self.get(request, self.template_name)

            elif sum != 100:
                messages.warning(self.request,
                "The sum of compounds' mass percentage is not equal to 100%, this might affect the property predicted.")
            else:
                messages.success(self.request,
                "Property predicted successfully.")

            self.context['result'] = murnaghan_equation_predict(intensive_parameters, compounds)

            return render(request, self.template_name, self.context)