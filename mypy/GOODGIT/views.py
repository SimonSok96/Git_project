from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile

def home(request):
    return render(request, 'home.html', {})

def profiles(request):
    if request.user.is_authenticated:
        l = Profile.objects.exclude(user=request.user)
        return render(request, 'Profilepages.html', {"list_profile":l})
    else:
        messages.success(request, ("You ougth to be singed in!"))
        return redirect("home")
    
def someonesprofile(request, pk):
    if request.user.is_authenticated:
        l = Profile.objects.get(pk=pk)
        return render(request, 'someonesprofile.html', {"profile":l})
    else:
        messages.success(request, ("You ougth to be singed in!"))
        return redirect("home")