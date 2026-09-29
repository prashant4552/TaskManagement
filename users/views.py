from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task


def login_view(request):

    print("REQUEST METHOD:", request.method)

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("AUTHENTICATED USER:", user)

        if user is not None:
            print("LOGIN SUCCESS")
            login(request, user)
            return redirect('dashboard')

        else:
            print("LOGIN FAILED")

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid username or password.'
                }
            )

    return render(request, 'login.html')

@login_required
def dashboard(request):

    tasks = Task.objects.all()

    return render(
        request,
        'dashboard.html',
        {
            'tasks': tasks
        }
    )

@login_required
def create_task(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        Task.objects.create(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date
        )

        return redirect('dashboard')

    return render(request, 'create_task.html')

@login_required
def edit_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == 'POST':

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')
        task.due_date = request.POST.get('due_date')

        task.save()

        return redirect('dashboard')

    return render(
        request,
        'edit_task.html',
        {
            'task': task
        }
    )

@login_required
def delete_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == 'POST':

        task.delete()

        return redirect('dashboard')

    return render(
        request,
        'delete_task.html',
        {
            'task': task
        }
    )