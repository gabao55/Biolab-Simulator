from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
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