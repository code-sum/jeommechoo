from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Restaurant
from .forms import RestaurantForm
from django.http import HttpResponseForbidden
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
    context = {
        'restaurant': restaurant
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