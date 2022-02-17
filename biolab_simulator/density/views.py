from django.shortcuts import render
from django.views.generic import DetailView
from . import models

# Create your views here.
def density(request):
    template_name = 'density/density.html'
    return render(request, template_name)


class PredictiveModel(DetailView):
    model = models.PredictiveModel
    template_name = 'density/model.html'
    context_object_name = 'model'
    predictive_model = 'name'