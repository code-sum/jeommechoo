from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST
from .models import Restaurant
from reviews.models import Review
from .forms import RestaurantForm
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.decorators import login_required
import requests 
from django.db.models import Avg, Count

@require_safe
def index(request):
    sort = request.GET.get('sort','')
    if sort == '1':
        restaurants = Restaurant.objects.filter(category=1).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '2':
        restaurants = Restaurant.objects.filter(category=2).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '3':
        restaurants = Restaurant.objects.filter(category=3).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '4':
        restaurants = Restaurant.objects.filter(category=4).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '5':
        restaurants = Restaurant.objects.filter(category=5).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '6':
        restaurants = Restaurant.objects.filter(category=6).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '7':
        restaurants = Restaurant.objects.filter(category=7).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '8':
        restaurants = Restaurant.objects.filter(category=8).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '9':
        restaurants = Restaurant.objects.filter(category=9).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '10':
        restaurants = Restaurant.objects.filter(category=10).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    elif sort == '11':
        restaurants = Restaurant.objects.filter(category=11).annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)
    else:
        restaurants = Restaurant.objects.annotate(reviews_count=Count('review')).annotate(avg_grade=Avg('review__grade')).order_by('-pk')
        rankers = Restaurant.objects.annotate(avg_grade=Avg('review__grade')).order_by('-avg_grade')[:10]
        context = {
            'restaurants': restaurants,
            'rankers': rankers
        }
        return render(request, 'restaurants/index.html', context)

@require_safe
def detail(request, pk):
    # api 불러올거면 import requests 해줘야함 requests 하려면 pip install requests 해줘야합니당
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = Review.objects.filter(restaurant=restaurant) # 역참조 용환님체고 현중님 따따봉 태호님 진짜멋져
    # 리뷰 작성자들이 남긴 평점평균
    avg_grade_query = review.aggregate(Avg('grade'))
    avg_grade = avg_grade_query['grade__avg']

    client_id = 'lu249px3lh';    # 본인이 할당받은 ID 입력
    client_pw = 'LhI9orA8JVX5xIE1TJuRfKRFPyQcr8vqH2AzsNXq';    # 본인이 할당받은 Secret 입력

    endpoint = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    url = f"{endpoint}?query={restaurant.address}"

    headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id, 
    "X-NCP-APIGW-API-KEY": client_pw,
    }

    res = requests.get(url, headers=headers)
    lat = str(res.json()['addresses'][0]['y'])
    lng = str(res.json()['addresses'][0]['x'])
    
    context = {
        'lat' : lat,
        'lng' : lng,
        'restaurant': restaurant,
        'reviews': review,
        'avg_grade': avg_grade,
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
