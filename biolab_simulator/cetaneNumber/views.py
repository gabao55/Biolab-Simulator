from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from django.contrib import messages
from . import models
from .utils import lapuerta_rodriguez_predict


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

            if sum(volumes) != 100:
                messages.warning(self.request,
                "The sum of compounds' volume percentage is not equal to 100%, this might affect the property predicted.")

            return render(request, self.template_name, self.context)