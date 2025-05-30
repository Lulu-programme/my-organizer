from django.shortcuts import render, redirect

from tasks.models import Task
from myOrganizer.tools import tasks_category, tasks_priority

data_tasks = {
    'title': '',
    'category': '',
    'priority': 0,
    'description': '',
    'notes': '',
    'completed': False,
}


def index(request):

    # Importations
    task_list = Task.objects.filter(completed=False).order_by('category')

    context = {
        'title': 'Mes tâches',
        'tasks': task_list if task_list else None,
    }

    return render(request, 'tasks/index.html', context)


def add_task(request):

    data = data_tasks.copy()

    if request.method == 'POST':
        data['title'] = request.POST.get('title')
        data['category'] = request.POST.get('category')
        data['priority'] = int(request.POST.get('priority'))
        data['description'] = request.POST.get('description')
        data['notes'] = request.POST.get('notes')

        task = Task(**data)
        task.save()

        return redirect('home')

    context = {
        'title': 'Ajouter une tâche',
        'categories': tasks_category,
        'priorities': tasks_priority,
    }

    return render(request, 'tasks/add_task.html', context)

def modify_task(request, task_id):

    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.category = request.POST.get('category')
        task.priority = int(request.POST.get('priority'))
        task.description = request.POST.get('description')
        task.notes = request.POST.get('notes')

        task.save()

        return redirect('home')

    context = {
        'title': f'Modification de {task.title}',
        'task': task,
        'categories': tasks_category,
        'priorities': tasks_priority,
    }

    return render(request, 'tasks/modify_task.html', context)

def view_task(request, task_id):

    task = Task.objects.get(id=task_id)

    context = {
        'title': f'Tache : {task.title}',
        'task': task,
    }

    return render(request, 'tasks/view_task.html', context)
