from django.shortcuts import render

# Create your views here.

def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')

def home(request):
    return render(request, 'base/home.html')