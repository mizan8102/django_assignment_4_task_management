from django.shortcuts import render,redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm

# Create your views here.
def home(request)->render:
    data = TaskModel.objects.all()
    return render(request, 'task/list.html', { 'data' : data})

# save task 
def save(request)->render:
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    form = TaskForm()
    return render(request, 'task/add.html', { 'form' : form })
    

# edit task 
def edit(request, id:int)->render:
    try:
        task = get_object_or_404(TaskModel, pk=id)
        
        if request.method == 'POST':
            formTask = TaskForm(request.POST, instance=task)
            if formTask.is_valid():
                formTask.save()
                return redirect('home')
        else:  
            formTask = TaskForm(instance=task)
        return render(request, 'task/add.html', { 'form': formTask})
    except Exception as e:
            return render(request, 'task/add.html', { 'errors': e})


# delete task 
def delete(request, id:int)->redirect:
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('home')
    
