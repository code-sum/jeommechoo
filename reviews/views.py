from django.shortcuts import render, redirect, get_object_or_404
from reviews.models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from restaurants.models import Restaurant
from django.views.generic.list import ListView
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages

class ReviewsView(ListView):
    model =Review
    paginate_by = 3
    context_object_name = 'reviews'
    template_name = 'reviews/index.html'
    ordering = ['-pk']
    
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)

def detail(request, pk):
    # 특정 글을 가져온다.
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "review": review,
        "comments": review.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "reviews/detail.html", context)

@login_required
def create(request, restaurant_pk):
    restaurants = Restaurant.objects.get(pk=restaurant_pk)
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurants
            review.save()
            return redirect("restaurants:detail", restaurants.pk)
    else:
        review_form = ReviewForm()
    context = {
    "review_form": review_form,
    }
    return render(request, "reviews/new.html", context=context)

@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == "POST":
            # POST : input 값 가져와서, 검증하고, DB에 저장
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                review_form.save()
                return redirect("reviews:detail", review.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
        else:
            # GET : Form을 제공
            review_form = ReviewForm(instance=review)
        context = {"review_form": review_form,}
        return render(request, "reviews/update.html", context)
    else:
        # 작성자가 아닐 때
        # (1) 403 에러메시지를 던져버린다.
        # from django.http import HttpResponseForbidden
        # return HttpResponseForbidden()
        # (2) flash message 활용!
        return redirect("reviews:detail", review.pk)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        review = Review.objects.get(pk=pk)
        if request.user == review.user:
            review.delete()
    return redirect("restaurants:index")

@login_required
def comment_create(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect("reviews:detail", review.pk)

@login_required
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        if request.method == 'POST':
            comment.delete()
            return redirect("reviews:detail", pk)
    else:
        return HttpResponseForbidden()