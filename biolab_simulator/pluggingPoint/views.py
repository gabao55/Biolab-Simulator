from django.shortcuts import render

# Create your views here.
def pluggingPoint(request):
    template_name = 'pluggingPoint/pluggingPoint.html'
    return render(request, template_name)