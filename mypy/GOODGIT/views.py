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
        if request.method == "POST":
            action = request.POST["follow"]
            current_user = request.user.profile
            if action == "follow":
                current_user.follows.add(l)
            elif action == "unfollow":
                current_user.follows.remove(l)
            current_user.save()
        return render(request, 'someonesprofile.html', {"profile":l})
    else:
        messages.success(request, ("You ougth to be singed in!"))
        return redirect("home")