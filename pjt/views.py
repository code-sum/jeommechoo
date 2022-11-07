from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from restaurants.models import Restaurant
import random
from django.contrib.auth import login as auth_login
from django.contrib import messages

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
    return render(request, 'random.html')

def developers(request):
    return render(request, 'developers.html')