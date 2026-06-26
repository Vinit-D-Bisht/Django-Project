from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks

# Create your views here.

def home(request):
    if request.method == "POST":
        task = request.POST["task"]
        Tasks.objects.create(title=task)
        return redirect("/")

    task = Tasks.objects.all()
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
