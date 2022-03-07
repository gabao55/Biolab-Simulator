from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from . import models

def cetaneNumber(request):
    template_name = 'cetaneNumber/cetaneNumber.html'
    return render(request, template_name)
class CetaneNumber(View):
    template_name = 'cetaneNumber/cetaneNumber.html'

    def get(self, request, *args, **kwargs):
        predictive_models = models.PredictiveModel.objects.all
        context = {'predictive_models': predictive_models,}

        return render(request, self.template_name, context)

class PredictiveModel(DetailView):
    model = models.PredictiveModel
    template_name = 'cetaneNumber/model.html'
    context_object_name = 'model'

    def get_object(self):
        self.model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        return self.model