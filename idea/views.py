from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
from program.models import Program
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')


def ideaView(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea': idea,
    }
    return render(request, 'idea/idea.html', context)


def ideaCreate(request, pk):
    program = Program.objects.get(id=pk)
    form = IdeaForm()
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        idea = form.save(commit=False)
        idea.program = program
        idea.business_unit = idea.program.business_unit
        idea.ideator = request.user
        if form.is_valid():
            idea.save()
            return redirect('idea', idea.id)
    context = {
        'form': form,
    }
    return render(request, 'idea/idea_form.html', context)

def ideaList(request):
    ideas = Idea.objects.all()
    context = {
        'ideas' : ideas,
    }
    return render(request, 'idea/idea_list.html', context)
