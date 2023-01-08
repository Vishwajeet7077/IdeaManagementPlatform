from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')


def login(request):
    return render(request, 'account/login.html')


def register(request):
    if request.method == 'GET':
        user_form = UserCreationForm()
        profile_form = ProfileForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'account/register.html', context)
    else:
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.user = user
            user.save()
            profile.save()
            return redirect('home')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(request, 'account/register.html', context)


def profile(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user,
    }
    return render(request, 'account/profile.html', context)


def profileList(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'account/profile_list.html', context)


def profileUpdate(request, pk):
    profile = Profile.objects.get(id=pk)
    profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save()
            return redirect('profile', profile.id)
        else:
            print(profile_form.errors)
    context = {
        'profile_form' : profile_form,
        'error_messages' : profile_form
    }
    return render(request, 'account/profile_form.html', context)
