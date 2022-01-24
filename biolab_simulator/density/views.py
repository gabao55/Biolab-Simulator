from django.shortcuts import render

# Create your views here.
def density(request):
    template_name = 'density/density.html'
    return render(request, template_name)
