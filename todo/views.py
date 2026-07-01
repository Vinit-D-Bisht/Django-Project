from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    if request.method == "POST":
        task = request.POST["task"]
        Tasks.objects.create(user=request.user,title=task)
        return redirect("/")

    task = Tasks.objects.filter(user=request.user)
    return render(request, "home.html", {"tasks": task})

def delete(request, id):
    Tasks.objects.get(id=id).delete()
    return redirect("/")

def edit(request, id):
    task = Tasks.objects.get(id=id)

    if request.method == "POST":
        task.title = request.POST["task"]
        task.save()
        return redirect("/")

    return render(request, "edit.html", {"task": task})

def status(request, id):
    task = Tasks.objects.get(id=id)
    task.status = not task.status
    task.save()
    return redirect("/")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("/login/")

    return render(request, "register.html")

def loginuser(request):
    if request.method == "POST":
        username =request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request ,user)
            return redirect('/')

    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    return redirect('/login/')
