from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from . import models
from .utils import chhetri_watts_predict, molecular_structure_predict, murnaghan_equation_predict, rackett_soave_predict


class Density(View):
    template_name = 'density/density.html'

    def get(self, request, *args, **kwargs):
        density_models = models.PredictiveModel.objects.all
        context = {'density_models': density_models,}

        return render(request, self.template_name, context)


class MurnaghanEquation(DetailView):
    template_name = 'density/murnaghan_equation.html'
    model = get_object_or_404(models.PredictiveModel,
        name='Equação de Murnaghan')

    intensive_parameters = ['Temperatura (K)', "Pressão (MPa)", "Massa específica atmosférica (kg/m³)"]
    context = {
        'model': model,
        'intensive_parameters': intensive_parameters,
    }

    def get(self, request, *args, **kwargs):

        self.context['result'] = None

        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()
            
            intensive_parameters = {"Temperature": float(form["Temperatura (K)"]) if form['Temperatura (K)'] else '',
            "Pressure": float(form["Pressão (MPa)"]) if form["Pressão (MPa)"] else '',
            "Atmospheric density": float(form["Massa específica atmosférica (kg/m³)"]) if form["Massa específica atmosférica (kg/m³)"] else '',
            }
            
            if not intensive_parameters['Temperature'] \
            or not intensive_parameters['Pressure'] \
            or not intensive_parameters['Atmospheric density']:
                messages.error(self.request,
                "Insira todos os parâmetros intensivos para prever a propriedade")

                return self.get(request, self.template_name)

            form.pop("Temperatura (K)")
            form.pop("Pressão (MPa)")
            form.pop("Massa específica atmosférica (kg/m³)")
            form.pop("compounds")

            compounds = {}
            sum = 0
            for compound, value in form.items():
                if compound != 'csrfmiddlewaretoken' and value and float(value):
                    compounds[compound] = {'composition': float(value)}
                    sum += float(value)

                    parameters_set = self.model.compound_set.get(esther_type=compound.split(' ')[0], name=compound.split(' ')[1]).parameter_set.all()

                    for parameter in parameters_set:
                        compounds[compound][parameter.name] = parameter.value
            
            if not compounds:
                messages.error(self.request,
                "Insira a porcentagem de massa dos compostos para prever a propriedade")

                return self.get(request, self.template_name)

            elif sum != 100:
                messages.warning(self.request,
                "A soma da porcentagem em massa dos compostos não é igual a 100%, isso pode afetar a propriedade prevista.")
            else:
                messages.success(self.request,
                "Propriedade prevista com sucesso.")

            self.context['result'] = murnaghan_equation_predict(intensive_parameters, compounds)

            return render(request, self.template_name, self.context)

class ChhetriWatts(DetailView):
    template_name = 'density/chhetri_watts.html'
    model = get_object_or_404(models.PredictiveModel,
        name='Chhetri & Watts')
    context = {
        'model': model,
    }

    def get(self, request, *args, **kwargs):

        self.context['result'] = None

        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = request.POST.dict()

            temperature = float(form['Temperature'])
            pressure = float(form['Pressure'])

            self.context['result'] = chhetri_watts_predict(temperature, pressure)

            return render(request, self.template_name, self.context)

class RackettSoave(MurnaghanEquation):
    template_name = 'density/murnaghan_equation.html'
    model = get_object_or_404(models.PredictiveModel,
        name='Método Rackett-Soave')

    intensive_parameters = ['Temperatura (K)', "Temperatura de Referência (K)", "Massa específica de referência (kg/m³)"]
    context = {
        'model': model,
        'intensive_parameters': intensive_parameters,
    }

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()
            
            intensive_parameters = {"Temperature": float(form["Temperatura (K)"]) if form['Temperatura (K)'] else '',
            "Reference temperature": float(form["Temperatura de Referência (K)"]) if form["Temperatura de Referência (K)"] else '',
            "Reference density": float(form["Massa específica de referência (kg/m³)"]) if form["Massa específica de referência (kg/m³)"] else '',
            }

            if not intensive_parameters['Temperature'] \
            or not intensive_parameters['Reference temperature'] \
            or not intensive_parameters['Reference density']:
                messages.error(self.request,
                "Insira todos os parâmetros intensivos para prever a propriedade")

                return self.get(request, self.template_name)

            form.pop("Temperatura (K)")
            form.pop("Temperatura de Referência (K)")
            form.pop("Massa específica de referência (kg/m³)")
            form.pop("compounds")

            compounds = {}
            sum = 0
            for compound, value in form.items():
                if compound != 'csrfmiddlewaretoken' and value and float(value):
                    compounds[compound] = {'composition': float(value)}
                    sum += float(value)

                    parameters_set = self.model.compound_set.get(esther_type=compound.split(' ')[0], name=compound.split(' ')[1]).parameter_set.all()

                    for parameter in parameters_set:
                        compounds[compound][parameter.name] = parameter.value
            
            if not compounds:
                messages.error(self.request,
                "Insira a porcentagem de massa dos compostos para prever a propriedade")

                return self.get(request, self.template_name)
            elif sum != 100:
                messages.warning(self.request,
                "A soma da porcentagem em massa dos compostos não é igual a 100%, isso pode afetar a propriedade prevista.")
            else:
                messages.success(self.request,
                "Propriedade prevista com sucesso.")

            self.context['result'] = rackett_soave_predict(intensive_parameters, compounds)

            return render(request, self.template_name, self.context)


class MolecularStructure(DetailView):
    template_name = "density/molecular_structure.html"
    model = get_object_or_404(models.PredictiveModel,
        name = "Estrutura molecular")

    context = {
        "model": model,
    }

    def get(self, request, *args, **kwargs):

        self.context['result'] = None

        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()
            form.pop("csrfmiddlewaretoken")

            if not form:
                return render(request, self.template_name, self.context)

            self.context['result'], molar_fractions_sum = molecular_structure_predict(form)

            if sum(molar_fractions_sum) != 1:
                messages.warning(self.request,
                "A soma das frações molares dos compostos não é igual a 100%, isso pode afetar a propriedade prevista.")

            return render(request, self.template_name, self.context)