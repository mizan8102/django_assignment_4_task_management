from django.shortcuts import render,redirect, get_object_or_404
from .forms import CategoryForm
from .models import CategoryModel

# Create your views here.
def list_category(reqeust):
    data = CategoryModel.objects.all()
    return render(reqeust, 'category/lists.html', { 'data' : data})

# add category 
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lsit_category')
    
    form = CategoryForm();
    return render(request, 'category/add.html', { 'form': form})


# edit post 
def edit_category(request, id):
    try:
        category = get_object_or_404(CategoryModel, pk=id)
        
        if request.method == 'POST':
            formCategory = CategoryForm(request.POST, instance=category)
            if formCategory.is_valid():
                formCategory.save()
                return redirect('lsit_category')
        else:  
            formCategory = CategoryForm(instance=category)
            
        return render(request, 'category/add.html', { 'form': formCategory})
    except Exception as e:
            return render(request, 'category/add.html', { 'errors': e})


# delete post 
def delete_category(request, id):
    category = CategoryModel.objects.get(pk=id)
    category.delete()
    return redirect('lsit_category')