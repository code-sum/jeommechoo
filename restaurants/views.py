from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST
from .models import Restaurant
from reviews.models import Review
from .forms import RestaurantForm
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.decorators import login_required

def index(request):
    # 일단 가장 최근에 등록한 식당이 맨 앞에 오도록(추후 별점 반영해서 수정)
    restaurants = Restaurant.objects.order_by('-pk')
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

@require_safe
def detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    reviews = restaurant.restaurant.all() # 역참조 용환님체고 현중님 따따봉 태호님 진짜멋져
    print(restaurant)
    context = {
        'restaurant': restaurant,
        'reviews': reviews,
    }
    return render(request, 'restaurants/detail.html', context)

@login_required
def create(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    else:
        if request.method == 'POST':
            form = RestaurantForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('restaurants:index')
        else:
            form = RestaurantForm()
        context = {
            'form': form
        }
        return render(request, 'restaurants/new.html', context)

@login_required
def update(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    else:
        restaurant = get_object_or_404(Restaurant, pk=pk)
        if request.method == 'POST':
            form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
            if form.is_valid():
                form.save()
                return redirect('restaurants:detail', restaurant.pk)
        else:
            form = RestaurantForm(instance=restaurant)
        context = {
            'form': form
        }
        return render(request, 'restaurants/update.html', context)

@login_required
def delete(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    else:
        restaurant = get_object_or_404(Restaurant, pk=pk)
        if request.method == 'POST':
            restaurant.delete()
            return redirect('restaurants:index')
        else:
            return HttpResponseForbidden()

@login_required
def like(request, pk):
    if request.user.is_authenticated:
        restaurant = get_object_or_404(Restaurant, pk=pk)
        if restaurant.like_users.filter(pk=request.user.pk).exists():
            restaurant.like_users.remove(request.user)
            is_liked = False
        else:
            restaurant.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
            'likeCount': restaurant.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')
