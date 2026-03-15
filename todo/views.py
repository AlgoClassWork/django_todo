from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks' : tasks} )

def add_task(request):
    data = request.POST.get('title')
    Task.objects.create(title=data)
    return redirect( home )