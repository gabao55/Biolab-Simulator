from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View

from .utils import su_liu_predict
from . import models

def pluggingPoint(request):
    template_name = 'pluggingPoint/pluggingPoint.html'
    return render(request, template_name)



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