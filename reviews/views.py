from .models import Review
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostReviewForm
# from django.contrib.auth.mixins import LoginRequiredMixin


def all_reviews(request):
    stuff = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews.html', stuff)


def single_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'single-review.html', {'review': review})


def new_review(request, pk=None):
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = PostReviewForm(request.POST, request.FILES, instance=review)
        form.instance.author = request.user
        if form.is_valid():
            review = form.save()
            return redirect(single_review, review.pk)
    else:
        form = PostReviewForm(instance=review)
        form.instance.author = request.user
    return render(request, 'addreview.html', {'form': form})
