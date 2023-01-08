from django.shortcuts import render, redirect
from .models import Program
from .forms import ProgramForm, BusinessUnitForm
from idea.models import Idea
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')


def programList(request):
    programs = Program.objects.all()
    context = {
        'programs': programs,
    }
    return render(request, 'program/program_list.html', context)


def programView(request, pk):
    program = Program.objects.get(id=pk)
    ideas = Idea.objects.filter(program=program)
    context = {
        'program': program,
        'ideas' : ideas,
    }
    return render(request, 'program/program.html', context)


def programCreate(request):
    if request.method == 'GET':
        form = ProgramForm()
        context = {
            'form': form,
        }
        return render(request, 'program/program_form.html', context)
    else:
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.save()
            return redirect('program', program.id)
        else:
            context = {
                'form' : form,
            }
            return render(request, 'program/program_form.html', context)

def programUpdate(request, pk):
    program = Program.objects.get(id=pk)
    print(program.name)
    if request.method == 'GET':
        form = ProgramForm(instance=program)
        context = {
            'form': form,
        }
        return render(request, 'program/program_form.html', context)
    else:
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program', program.id)
        context = {
            'form': form
        }
        return render(request, 'program/program_form.html', context)


def programDelete(request, pk):
    program = Program.objects.get(id=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program-list')
    else:
        context = {
            'program' : program,
        }
        return render(request, 'program/program_delete_confirmation.html')