from django.shortcuts import render

def pluggingPoint(request):
    template_name = 'pluggingPoint/pluggingPoint.html'
    return render(request, template_name)