from django.shortcuts import render
from program.models import BusinessUnit
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')


def home(request):
    business_units = BusinessUnit.objects.all()
    context = {
        'business_units': business_units,
    }
    return render(request, 'base/home.html', context)
