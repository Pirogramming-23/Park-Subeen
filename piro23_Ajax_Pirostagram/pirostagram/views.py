from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment, Like
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def post_list(request):
    posts = Post.objects.all()
    liked_post_ids = []

    if request.user.is_authenticated:
        liked_post_ids = [like.post.id for like in request.user.like_set.all()]

    return render(request, 'post_list.html', {
        'posts': posts,
        'liked_post_ids': liked_post_ids
    })

@require_POST
def toggle_like(request):
    post = get_object_or_404(Post, id=request.POST['post_id'])
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({'liked': liked, 'like_count': post.likes.count()})

@require_POST
def add_comment(request):
    post = get_object_or_404(Post, id=request.POST['post_id'])
    comment = Comment.objects.create(post=post, author=request.user, text=request.POST['text'])
    return JsonResponse({'id': comment.id, 'author': comment.author.username, 'text': comment.text})

@require_POST
def delete_comment(request):
    comment = get_object_or_404(Comment, id=request.POST['comment_id'])
    if comment.author == request.user:
        comment.delete()
        return JsonResponse({'deleted': True})
    return JsonResponse({'deleted': False}, status=403)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('post_list')
    return render(request, 'logout.html') 
