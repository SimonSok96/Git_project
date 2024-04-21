from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Profile, Tweet
from .forms import TweetForm, RegisterForm, ProfileForm

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
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You have succsessfully loged out"))
    return redirect("home")

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, ("You have succsessfully sing in"))
            return redirect("home")
    return render(request, 'register.html', {'form': form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        profile = Profile.objects.get(user__id = request.user.id)
        form = RegisterForm(request.POST or None, request.FILES or None, instance = current_user)
        profileform = ProfileForm(request.POST or None, request.FILES or None, instance = profile)
        if form.is_valid() and profileform.is_valid():
            form.save()
            profileform.save()
            login(request, current_user)
            messages.success(request, ("You have succsessfully change your profile"))
            return redirect("home")

        return render(request, 'update_user.html', {'form': form, 'profileform': profileform})
    else:
        messages.success(request, ("You should to be logged in"))
        return redirect("home")
    
    
def TweetLike(request, pk):
    if request.user.is_authenticated:
        tweet = get_object_or_404(Tweet, id=pk)
        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user)
        else:
            tweet.likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, ("You should to be logged in"))
        return redirect("home")
