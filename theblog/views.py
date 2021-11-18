from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Comment, Post, Category, Like, DisLike
from .forms import CommentForm, UserPost

# List
def post_list(request):
    # posts = Post.objects.all()  # bütün postları getirir, biz sadece publish olanaları istiyoruz
    # posts = Post.objects.filter(status='p')  # published olanlara databese p olarak kaydediliyor. o yüzden p olarak çağırıyoruz
    list_post = Post.objects.filter(status='p')
    p = Paginator(list_post, 4)
    page = request.GET.get('page')
    post_p = p.get_page(page)
    nums = ' ' * post_p.paginator.num_pages
    context = {
        # 'user_posts' : posts,
        'post_p' : post_p,
        'nums' : nums
    }
    return render(request, 'theblog/post_list.html', context)

# Details
def post_details(request, id):
    # print(request.user)
    # print(request.path)
    form = CommentForm()
    post = get_object_or_404(Post, id=id)
    # post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # kaydedecek ama databese göndermeyecek
            comment.user = request.user
            comment.post = post 
            comment.save()
            return redirect('theblog:details', id=id)
    context = {
        'user_post' : post,
        'comment_form' : form
    }
    return render(request, 'theblog/post_details.html', context)

# Create
def post_add(request):
    form = UserPost() 
    if request.method == 'POST':
        form = UserPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # form.save()
            return redirect ('theblog:home')
    context = {
        'user_form' : form
    }
    return render(request, 'theblog/post_add.html', context)

# Update
def post_update(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    if request.user.id != post.author.id:
        return redirect('theblog:home')
    form = UserPost(instance=post)
    if request.method == 'POST': 
        form = UserPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect ('theblog:home')
    context = {
        'user_form_update' : form,
        'user_post_update' : post
    }
    return render(request, 'theblog/post_update.html', context)

# Delete
def post_delete(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    if request.user.id != post.author.id:
        return redirect('theblog:home')
    if request.method == 'POST':
        post.delete()
        return redirect ('theblog:home')
    context = {
        'user_post_delete' : post
    }
    return render(request, 'theblog/post_delete.html', context)

# Like
def post_like(request, id):
    if request.method == 'POST':
        post_lk = get_object_or_404(Post, id=id)
        like = Like.objects.filter(user=request.user, post=post_lk)
        if like:  # like ettiysek delete edecek
            like[0].delete()  # obj olduğu için içindeki elemana ulaşabilmek için [0] yazdık
        else:
            Like.objects.create(user=request.user, post=post_lk)
        return redirect('theblog:details', id=id)

def post_dislike(request, id):
    if request.method == 'POST':
        post_dlk = get_object_or_404(Post, id=id)
        dlike = DisLike.objects.filter(user=request.user, post=post_dlk)
        if dlike: # like ettiysek delete edecek
            dlike[0].delete()  # obj olduğu için içindeki elemana ulaşabilmek için [0] yazdık
        else:
            DisLike.objects.create(user=request.user, post=post_dlk)
        return redirect('theblog:details', id=id)

