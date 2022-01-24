from django.shortcuts import render

# Create your views here.
def cetaneNumber(request):
    template_name = 'cetaneNumber/cetaneNumber.html'
    return render(request, template_name)