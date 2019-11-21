from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
import random
from .forms import SignupForm, LoginForm, TipForm
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Tip, Upvote, Downvote
from django.forms.models import model_to_dict

# Create your views here.

def home(request):
    tips = Tip.objects.all().order_by('date')
    if request.method == 'POST':
        if 'deletetip' in request.POST:
            # print("removal request for a tip")
            if (request.user.has_perm('ex.deletetip') or
                    model_to_dict(Tip.objects.get(
                        id=request.POST['tipid'])).get('auteur') ==
                    request.user.username):
                form = TipForm()
                t = Tip.objects.filter(id=request.POST['tipid'])
                t.delete()
        elif 'upvote' in request.POST:
            # print("upvote request")
            form = TipForm()
            ts = Tip.objects.filter(id=request.POST['tipid'])
            if len(ts) > 0:
                t = ts[0]
                t.upvoteForUser(request.user.username)
        elif 'downvote' in request.POST:
            # print("downvote request")
            form = TipForm()
            ts = Tip.objects.filter(id=request.POST['tipid'])
            if len(ts) > 0:
                t = ts[0]
                t.downvoteForUser(request.user.username)
        else:
            form = TipForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                tip = Tip(content=data['content'], auteur=request.user.username)
                tip.save()
                # print('New Tip Created',tip)
            #return redirect('/')
    else: # method 'GET':
        # print("method 'GET':form = TipForm()")
        form = TipForm()
    if request.COOKIES.get('mycookie'):
        # print("if request.COOKIES.get('mycookie')")
        usador = request.COOKIES['mycookie']
        response = render(request, 'ex/index.html', {'usador': usador, 'tips': tips, 'form': form})
    else:
        # print("else: ...request.COOKIES.get('mycookie')")
        usador = random.choice(settings.USER_NAMES)
        response = render(request, 'ex/index.html', {'usador': usador, 'tips': tips, 'form': form})
        response.set_cookie('mycookie', usador, max_age=settings.SESSION_COOKIE_DURATION)

    return response


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = auth.authenticate(username=data['username'], password=data['password'])
            if u and u.is_active:
                auth.login(request, u)
                print('User logged in')
                return redirect('/')
            else:
                print('Unknown or inactive user')
                form._errors['username'] = ['Unknown or inactive user']
    else: # method 'GET':
        print("method 'GET': form = LoginForm()")
        form = LoginForm()

    return render(request, 'ex/login.html', {'usador': request.user, 'form': form, })

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(username=data['username'], password=data['password'])
            u.save()
            auth.login(request, u)
            # print('User created and logged in ', u)

            return redirect('/')
    else: # method 'GET':
        # print("method 'GET': form = SignupForm()")
        form = SignupForm()

    return render(request, 'ex/signup.html', {'usador': request.user, 'form': form, })


def logout(request):
    auth.logout(request)
    return redirect('/')