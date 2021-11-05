from django.shortcuts import redirect, render
from .models import Post, Category
from .forms import UserPost

def home(request):
    return render(request, 'base.html', {})

def post_list(request):
    posts = Post.objects.all()
    context = {
        'user_posts' : posts
    }
    return render(request, 'theblog/post_list.html', context)

def post_details(request, id):
    post = Post.objects.get(id=id)
    context = {
        'user_post' : post
    }
    return render(request, 'theblog/post_details.html', context)

def post_add(request):
    form = UserPost()
    if request.method == 'POST':
        form = UserPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('list')
    context = {
        'user_form' : form
    }
    return render(request, 'theblog/post_add.html', context)

def post_update(request, id):
    post = Post.objects.get(id=id)
    form = UserPost(instance=post)
    if request.method == 'POST': 
        form = UserPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect ('list')
    context = {
        'user_form_update' : form,
        'user_post_update' : post
    }

    return render(request, 'theblog/post_update.html', context)

def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect ('list')
    context = {
        'user_post_delete' : post
    }
    return render(request, 'theblog/post_delete.html', context)