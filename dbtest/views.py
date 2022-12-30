import data as data
from django.http import HttpResponse
from django.template import loader
from . import forms
from .models import Posts

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    latest_Post = Posts.objects.all()
    context = {'latest_Post': latest_Post}
    return render(request, 'Posts/index.html', context)

@login_required
def newPost(request):
    context = {}

    # create object of form
    form = forms.NewPost(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "new.html", context)


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user:
                login(request, user)
                return redirect('Posts:index')

    return render(request, 'Posts/login.html', {
        'form': form,
    })
@login_required
def logout_view(request):
    logout(request)
    return redirect('Posts:index')


