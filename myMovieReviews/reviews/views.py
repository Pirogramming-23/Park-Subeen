from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('reviews:review_list')
