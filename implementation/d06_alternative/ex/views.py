from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import random

from .forms import UserLoginForm, CreateTipForm
from .models import Tip, UserVotes, Reputation


def index(request):
    tips = Tip.objects.order_by('-created').all()
    if request.user.is_authenticated:
        tipForm = CreateTipForm()
        response = render(request, 'ex/index.html', {'form': tipForm, 'tips': tips})
    else:
        response = render(request, 'ex/index.html', {'tips': tips})
    if 'username' not in request.COOKIES:
        username = random.choice(settings.USERNAMES)
        response.set_cookie('username', username, max_age=settings.USERNAME_DURATION)
    return response


def signin(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'ex/login.html', {'form': form, 'error': 'False login/password'})
    else:
        form = UserLoginForm()
    return render(request, 'ex/login.html', {'form': form})


def signout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/')


def signup(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            r = Reputation(user=user)
            r.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'ex/signup.html', {'form': form})


def createtip(request):
    if request.user.is_authenticated() and request.method == 'POST':
        form = CreateTipForm(request.POST)
        text = form.data.get('text')
        author = request.user
        if text:
            tip = Tip(author=author, text=text)
            tip.save()
    return redirect('/')


def vote(request):
    if request.method == 'GET' and request.user.is_authenticated():
        tip = Tip.objects.get(id=request.GET['id'])
        if request.user.reputation.rep >= 15 or request.user.username == tip.author.username:
            if int(request.GET['type']) == 1:
                tip.upvote(request.user)
            elif int(request.GET['type']) == -1:
                tip.downvote(request.user)
            tip.save()
    return redirect('/')


def delete(request):
    if request.method == 'GET' and request.user.is_authenticated():
        tip = Tip.objects.get(id=request.GET['id'])
        if tip.author.username == request.user.username or request.user.reputation.rep >= 30:
            tip_author_rep = tip.author.reputation
            if tip_author_rep.rep > 0:
                tip_author_rep.rep -= tip.votes * 5
            else:
                tip_author_rep.rep -= tip.votes * 2
            tip_author_rep.save()
            tip.delete()
    return redirect('/')
