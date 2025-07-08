from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request): # request 넘겨받아 render 메서드를 호출
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 변수 posts는 쿼리셋의 이름
    return render(request, 'blog/post_list.html', {'posts': posts})
    # 매개변수'posts'