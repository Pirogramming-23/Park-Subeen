# ideas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea, DevTool, IdeaStar
from .forms import IdeaForm, DevToolForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count

# 메인페이지 (아이디어 리스트)
def idea_list(request):
    order = request.GET.get('order', '-created_at')
    ideas = Idea.objects.all().annotate(stars_count=Count('stars')).order_by(order)

    # 로그인 사용자의 찜 상태
    user_starred_ids = []
    if request.user.is_authenticated:
        user_starred_ids = IdeaStar.objects.filter(user=request.user).values_list('idea_id', flat=True)

    paginator = Paginator(ideas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ideas/idea_list.html', {
        'page_obj': page_obj,
        'order': order,
        'user_starred_ids': list(user_starred_ids),
    })

# 아이디어 등록
@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('ideas:idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_form.html', {'form': form})

# 아이디어 디테일
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    starred = False
    if request.user.is_authenticated:
        starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
    return render(request, 'ideas/idea_detail.html', {
        'idea': idea,
        'starred': starred
    })

# 아이디어 수정
@login_required
def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/idea_form.html', {'form': form})

# 삭제
@login_required
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('ideas:idea_list')

# 찜하기 ajax
@login_required
def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    star, created = IdeaStar.objects.get_or_create(user=request.user, idea=idea)
    if not created:
        star.delete()
        status = 'removed'
    else:
        status = 'added'
    return JsonResponse({'status': status})

# 관심도 ajax
@login_required
def adjust_interest(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    delta = int(request.GET.get('delta', 0))
    idea.interest += delta
    idea.save()
    return JsonResponse({'interest': idea.interest})

# DevTool views
def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'ideas/devtool_list.html', {'devtools': devtools})

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    ideas = devtool.ideas.all()
    return render(request, 'ideas/devtool_detail.html', {
        'devtool': devtool,
        'ideas': ideas
    })

@login_required
def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('ideas:devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm()
    return render(request, 'ideas/devtool_form.html', {'form': form})

@login_required
def devtool_edit(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('ideas:devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'ideas/devtool_form.html', {'form': form})

@login_required
def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    devtool.delete()
    return redirect('ideas:devtool_list')
