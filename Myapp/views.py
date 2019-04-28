from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PostForm
# Create your views here.

def home(request):
    person = Person.objects
    return render(request, 'Myapp/home.html', {'person':person})

# def detail(request, post_id):
#     person_detail = get_object_or_404(Person, pk=post_id)
#     return render(request, 'Myapp/detail.html', {'person_detial': person_detail})

def new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'Myapp/new.html', {'form':form})

def detail(request, post_id):
    post = get_object_or_404(Person, pk=post_id)
    return render(request, 'Myapp/detail.html', {'person':post,})

def edit(request, post_id):
    post = get_object_or_404(Person, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post.pk)
    
    else:
        form = PostForm(instance = post)
    return render(request, 'Myapp/edit.html', {'form':form})

def delete(request, post_id):
    post = get_object_or_404(Person, pk=post_id)
    post.delete()
    return redirect('home')
