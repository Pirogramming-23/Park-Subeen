from django.shortcuts import render
# Create your views here.

def post_list(request): # request 넘겨받아 render 메서드를 호출
    return render(request, 'blog/post_list.html', {})