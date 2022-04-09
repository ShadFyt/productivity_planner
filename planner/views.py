from django.shortcuts import redirect, render
from django.http import HttpResponse

from planner.models import Task

# Create your views here.


def home_page(request):
    if request.method == "POST":
        Task.objects.create(text=request.POST["task_text"])
        return redirect("/")

    tasks = Task.objects.all()

    return render(
        request, "home.html", {"tasks": tasks}  # template view  # content data
    )
