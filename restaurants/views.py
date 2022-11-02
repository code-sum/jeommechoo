from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Restaurant

def index(request):
    return render(request, 'restaurants/index.html')

@require_safe
def detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    context = {
        'restaurant': restaurant
    }
    return render(request, 'restaurants/detail.html', context)