from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required



def homepage(request):
    return render(request, 'homepage/homepage.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']

        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        if role == 'admin':
            user.is_staff = True
            user.is_superuser = True
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'homepage/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'homepage/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'homepage/todo_list.html', {'tasks': tasks, 'user': request.user})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
    return redirect('todo_list')

@login_required
def delete_task(request, pk):
    if request.user.is_staff:
        task = get_object_or_404(Task, pk=pk)
        task.delete()
    return redirect('todo_list')

@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('todo_list')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'homepage/task_detail.html', {'task': task})
