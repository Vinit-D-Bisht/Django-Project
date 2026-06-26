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
