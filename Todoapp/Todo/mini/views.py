from .forms import Todoforms
from .models import Todo
from django.shortcuts import render, redirect
from . models import Todo
# Create your views here.

def home(request):
    context = {}
    todolist = Todo.objects.all()
    context['todos'] = todolist

    return render(request, "index.html", context)



def add(request):
    
    
    
    
    if request.method == "POST":
     
        todoform = Todoforms(request.POST)

        if todoform.is_valid():
            
                new_todo = todoform.save(commit=False)
        
                new_todo.save()
                return redirect("home")

        else:
                todoform = Todoforms()
                return render(request, "index.html" , {"todoform":todoform})
    else:

        
        todoform = Todoforms()
        return render(request, "add.html" , {"todoform":todoform})


def edit(request, pk):
    todoapp = Todo.objects.get(pk = pk)
    formUpdate = Todoforms(request.POST, instance=todoapp)

    
    if request.method == "POST":
        if formUpdate.is_valid():
            formUpdate.save()
            return redirect("home")
        else:
            return render(request, "edit.html", {formUpdate: "formUpdate"})
    return render(request, "edit.html", {"formUpdate": formUpdate})


def delete(request, pk):

        todoapp = Todo.objects.filter(pk = pk)       
        todoapp.delete()
        return redirect("home")
    # return render(request, "delete.html", {"todoapp":todoapp })






        