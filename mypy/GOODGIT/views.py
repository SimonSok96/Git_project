from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Profile, Tweet
from .forms import TweetForm

def home(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, ("You have succssesfully added your tweet!"))
            return redirect("home")
        tweets = Tweet.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"tweets":tweets, "form": form})
    else:
        tweets = Tweet.objects.all().order_by("-created_at")
        messages.success(request, ("You ougth to be singed in!"))
        return render(request, 'home.html', {"tweets":tweets})
    

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
        I = Tweet.objects.filter(user_id=pk)
        if request.method == "POST":
            action = request.POST["follow"]
            current_user = request.user.profile
            if action == "follow":
                current_user.follows.add(l)
            elif action == "unfollow":
                current_user.follows.remove(l)
            current_user.save()
        return render(request, 'someonesprofile.html', {"profile":l, "tweets":I})
    else:
        messages.success(request, ("You ougth to be singed in!"))
        return redirect("home")
    
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have succsessfully loged in"))
            return redirect("home")
        else:
            messages.success(request, ("Wrong password or username"))
            return redirect("login")
    else:
        return render(request, 'login.html')