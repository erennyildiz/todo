from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from app.models import *
from django.db.models import F, Max

def home(request):
    todos = Todo.objects.all()
    return render(request, "index.html",{"todos":todos})

def addTodo(request):
    if request.method == "GET":
        return redirect("/")

    else:
        title = request.POST.get("title")
        # try:
        #     todo_id = Todo.objects.last().id + 1
        # except:
        #     todo_id = 1
        new_item = Todo(title = title, completed = False)

        new_item.save()
        return redirect("/")


def delete(request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        # objects = Todo.objects.filter(id__gt = todo_id)
        todo.delete()
        # objects.update(id=F('id') - 1)

        return redirect("/")