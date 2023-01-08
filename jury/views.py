from django.shortcuts import render, redirect
from idea.models import Idea
from program.models import Program, BusinessUnit
from account.models import Profile
from django.contrib.auth.models import User

# Create your views here.


def juryIdeaList(request):
    user = request.user
    programs = user.profile.jury_programs.all()
    ideas = Idea.objects.filter(id=-1)
    for program in programs:
        ideas = ideas | Idea.objects.filter(program=program)
    context = {
        'user': user,
        'programs': programs,
        'ideas': ideas,
    }
    return render(request, 'jury/jury_idea_list.html', context)

def ideaAccept(request, pk):
    user = request.user
    idea = Idea.objects.get(id=pk)
    if idea.program.business_unit.jury.contains(user):
        idea.accept()
        idea.save()
        return redirect('jury-idea-list')
    return redirect('unauthorized-access')

def ideaReject(request, pk):
    user = request.user
    idea = Idea.objects.get(id=pk)
    if idea.program.business_unit.jury.contains(user):
        idea.reject()
        idea.save()
        return redirect('jury-idea-list')
    return redirect('unauthorized-access')

def ideaPutOnHold(request, pk):
    user = request.user
    idea = Idea.objects.get(id=pk)
    if idea.program.business_unit.jury.contains(user):
        idea.putOnHold()
        idea.save()
        return redirect('jury-idea-list')
    return redirect('unauthorized-access')