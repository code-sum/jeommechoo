from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from restaurants.models import Restaurant
import random

def main(request):
    forms = AuthenticationForm()
    context = {
        'forms' : forms,
    }
    return render(request, "main.html", context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        restaurants = Restaurant.objects.filter(name__contains=searched)
        
        if  len(searched) == 0:
            restaurants = []
            text = "검색어를 입력하세요."

        elif len(restaurants) == 0:
            text = "검색 결과가 없습니다."
            
        else:
            text = ""
        return render(request, 'searched.html', {'restaurants': restaurants,'text':text})
    else:
        return render(request, 'searched.html', {})


def randomm(request):
    categogies = [
        '한식', '중식', '프렌치', '이탈리안', '스페니쉬', 
        '아메리칸', '튀르키예', '디저트', '멕시칸', '일식']
    random_category = random.choice(categogies)

    if random_category == '한식':
        random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_23.jpg'
    elif random_category == '중식':
        random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_9.jpg'
    elif random_category == '프렌치':
            random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_18.jpg'
    elif random_category == '이탈리안':
            random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_47.jpg'
    elif random_category == '스페니쉬':
            random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_33.jpg'
    elif random_category == '아메리칸':
            random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_30.jpg'
    elif random_category == '튀르키예':
            random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_16.jpg'
    elif random_category == '디저트':
            random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_22.jpg'
    elif random_category == '멕시칸':
            random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_27.jpg'
    else: # 일식
        random_imgs = 'http://www.lampcook.com/wi_files/food_top100/top5/5_3.jpg'

    context = {
        'menu': random_category,
        'imgs': random_imgs
    }

    return render(request, 'random.html', context)
