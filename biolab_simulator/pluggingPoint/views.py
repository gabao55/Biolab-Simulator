from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from django.contrib import messages
from .utils import li_bing_predict, sarin_predict, su_liu_predict
from . import models


class PluggingPoint(View):
    template_name = 'pluggingPoint/pluggingPoint.html'

    def get(self, request, *args, **kwargs):
        predictive_models = models.PredictiveModel.objects.all
        context = {'predictive_models': predictive_models,}

        return render(request, self.template_name, context)
        

class PredictiveModel(DetailView):
    model = models.PredictiveModel
    template_name = 'pluggingPoint/model.html'
    context_object_name = 'model'

    def get_object(self):
        self.model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        return self.model


class SuLiu(DetailView):
    template_name = "pluggingPoint/su_liu.html"
    model = get_object_or_404(models.PredictiveModel,
        name = "Su and Liu Correlation")

    context = {
        "model": model,
    }

    def get(self, request, *args, **kwargs):

        self.context['result'] = None

        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()

            self.context['result'] = su_liu_predict(form)

            if not form:
                return render(request, self.template_name, self.context)

            return render(request, self.template_name, self.context)

class Sarin(SuLiu):
    template_name = "pluggingPoint/sarin.html"
    model = get_object_or_404(models.PredictiveModel,
        name = "Sarin et al.")

    context = {
        "model": model,
    }
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()

            self.context['result'] = sarin_predict(form)

            if not form:
                return render(request, self.template_name, self.context)

            return render(request, self.template_name, self.context)

class LiBing(SuLiu):
    template_name = 'pluggingPoint/li-bing.html'
    model = get_object_or_404(models.PredictiveModel,
        name='Li-Bing et al.')

    context = {
        'model': model,
    }

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()

            compounds = {}
            sum = 0
            form.pop("compounds")
            
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

            self.context['result'] = li_bing_predict(compounds)

            return render(request, self.template_name, self.context)