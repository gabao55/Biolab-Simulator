from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from django.contrib import messages
from . import models
from .utils import freedman_bagdy_predict, lapuerta_rodriguez_predict, lapuerta_rodriguez_simplified_predict


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

        self.context['result'] = None

        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()
            form.pop("csrfmiddlewaretoken")

            if not form:
                return render(request, self.template_name, self.context)

            self.context['result'], volumes = lapuerta_rodriguez_predict(form)

            if sum(volumes) != 1:
                messages.warning(self.request,
                "A soma da porcentagem de volume dos compostos não é igual a 100%, isso pode afetar a propriedade prevista.")

            return render(request, self.template_name, self.context)

class LapuertaRodriguezSimplified(LapuertaRodriguez):
    template_name = "cetaneNumber/lapuerta_rodriguez_simplified.html"
    model = get_object_or_404(models.PredictiveModel,
        name = "La Puerta, Rodríguez and Mora (somente FAME)")

    context = {
        "model": model,
    }
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()
            form.pop("csrfmiddlewaretoken")

            if not form:
                return render(request, self.template_name, self.context)

            self.context['result'], volumes = lapuerta_rodriguez_simplified_predict(form)

            print(form)

            if sum(volumes) != 1:
                messages.warning(self.request,
                "A soma da porcentagem de volume dos compostos não é igual a 100%, isso pode afetar a propriedade prevista.")

            return render(request, self.template_name, self.context)

class FreedmanBagdy(LapuertaRodriguez):
    template_name = "cetaneNumber/freedman_bagdy.html"
    model = get_object_or_404(models.PredictiveModel,
        name = "Freedman and Bagdy")

    context = {
        "model": model,
    }
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.dict()
            form.pop("csrfmiddlewaretoken")

            if not form:
                return render(request, self.template_name, self.context)

            self.context['result'], volumes = freedman_bagdy_predict(form)

            print(form)

            if sum(volumes) != 1:
                messages.warning(self.request,
                "A soma da porcentagem de volume dos compostos não é igual a 100%, isso pode afetar a propriedade prevista.")

            return render(request, self.template_name, self.context)