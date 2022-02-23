from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from . import models

def density(request):
    template_name = 'density/density.html'
    return render(request, template_name)


class PredictiveModel(DetailView):
    model = models.PredictiveModel
    template_name = 'density/model.html'
    context_object_name = 'model'

    def get_object(self):
        self.model = get_object_or_404(models.PredictiveModel,
        name=self.kwargs['name'])
        return self.model