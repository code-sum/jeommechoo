from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Restaurant
from .forms import RestaurantForm

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

def create(request):
    if not request.user.is_superuser:
        return redirect('restaurants:index')
    else:
        if request.method == 'POST':
            form = RestaurantForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('restaurants:index')
        else:
            form = RestaurantForm()
        context = {
            'form': form
        }
        return render(request, 'restaurants/new.html', context)