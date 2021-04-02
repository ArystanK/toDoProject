from datetime import datetime

from django.shortcuts import render

from toDoApp.models import ToDoItem


def index(request):
    return render(request, 'index.html')


def all_todos(request):
    return render(request, 'list.html', context={'all_todos': ToDoItem.objects.all().order_by('-creation_date')})


def add_new_todo(request):
    to_do_item = ToDoItem()
    to_do_item.title = request.GET['title']
    to_do_item.description = request.GET['description']
    to_do_item.priority = request.GET['priority']
    to_do_item.creation_date = datetime.now()
    to_do_item.save()
    return all_todos(request)


def delete(request, pk):
    to_do_item = ToDoItem.objects.get(id=pk)
    to_do_item.delete()
    return all_todos(request)


def sort(request):
    return render(request, 'list.html', context={'all_todos': ToDoItem.objects.all().order_by('priority')})


def search(request):
    search_value = request.GET['search_value']
    return render(request, 'list.html',
                  context={'all_todos': ToDoItem.objects.all().filter(title__contains=search_value).order_by(
                      '-creation_date')})


def edit(request, pk):
    to_do_item = ToDoItem.objects.get(id=pk)
    item_detail = {
        'pk': to_do_item.pk,
        'title': to_do_item.title,
        'description': to_do_item.description,
        'priority': to_do_item.priority
    }
    return render(request, 'index.html', context=item_detail)


def safe_edit(request, pk):
    to_do_item = ToDoItem(id=pk)
    to_do_item.title = request.GET['title']
    to_do_item.description = request.GET['description']
    to_do_item.priority = request.GET['priority']
    to_do_item.creation_date = datetime.now()
    to_do_item.save()
    return all_todos(request)
