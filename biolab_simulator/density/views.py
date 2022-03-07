from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, View
from . import models


class Density(View):
    template_name = 'density/density.html'

    def get(self, request, *args, **kwargs):
        density_models = models.PredictiveModel.objects.all
        context = {'density_models': density_models,}

        return render(request, self.template_name, context)


class PredictiveModel(DetailView):
    model = models.PredictiveModel
    template_name = 'density/model.html'
    context_object_name = 'model'

    def get_object(self):
        self.model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        return self.model